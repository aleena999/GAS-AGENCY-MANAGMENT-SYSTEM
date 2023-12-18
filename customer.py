from flask import *
from database import *
customer=Blueprint('customer',__name__)
@customer.route('/customer_home')
def customer_home():
	return render_template('customer_home.html')
@customer.route('/connection_status',methods=['get','post'])
def connection_status():
	data={}
	q="select * from customer inner join cylinder_category using(cat_id)  where customer_id='%s'"%(session['customer_id'])
	res=select(q)
	data['profile']=res
	return render_template('customer_view_connection_status.html',data=data)
@customer.route('/send_complaint',methods=['get','post'])
def send_complaint():
	data={}
	if 'submit' in request.form:
		complaint=request.form['complaint']
		q="insert into complaint values(NULL,'%s','%s','pending',curdate())"%(session['customer_id'],complaint)
		insert(q)
		return redirect(url_for('customer.send_complaint'))
	q="select * from complaint where customer_id='%s'"%(session['customer_id'])
	res=select(q)
	data['complaints']=res
	return render_template('customer_send_complaint.html',data=data)
@customer.route('/book_gas',methods=['get','post'])
def book_gas():
	data={}
	q="select * from customer inner join cylinder_category using(cat_id)  where customer_id='%s'"%(session['customer_id'])
	res=select(q)
	data['profile']=res
	if 'submit' in request.form:
		q="select * from  booking where year(date)=year(curdate()) and month(date)=month(curdate()) and customer_id='%s'"%(session['customer_id'])
		res=select(q)
		if len(res)>=2:
			return "<script>alert('booking limit reached for this month!!!');window.location='/customer/customer_home';</script>"
		else:
			q="insert into booking values(NULL,'%s',curdate(),'pending')"%(session['customer_id'])
			insert(q)
			return "<script>alert('booking successfull!!!');window.location='/customer/customer_home';</script>"
	return render_template('customer_book_gas.html',data=data)

@customer.route('/bookings',methods=['get','post'])
def bookings():
	data={}
	q="select * from booking where customer_id='%s'"%(session['customer_id'])
	res=select(q)
	data['bookings']=res
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
		session['book_id']=id
	
	else:
		action=None
	if action=='payment':
		q="select * from customer inner join   cylinder_category using(cat_id) where customer_id='%s'"%(session['customer_id'])
		res=select(q)
		data['amount']=res
		print(res,",,,,,,,,,,,,,,,,,,")
		session['amount']=res[0]['price']
		return render_template('userpayment.html',data=data)
	return render_template('customer_view_bookings.html',data=data)

@customer.route('/gas_payment',methods=['get','post'])
def gas_payment():
	q="insert into payment values(NULL,'%s','%s','booking',curdate())"%(session['book_id'],session['amount'])
	insert(q)
	q="update booking set status='paid' where book_id='%s'"%(session['book_id'])
	update(q)
	return "<script>alert('Payment successfull!!!');window.location='/customer/bookings';</script>"


@customer.route('/book_service',methods=['get','post'])
def book_service():
	data={}
	q="select * from service"
	res=select(q)
	data['service']=res
	if 'submit' in request.form:
		service_id=request.form['service_id']
		q="insert into service_booking values(NULL,'%s','%s','pending',curdate())"%(session['customer_id'],service_id)
		insert(q)
		return "<script>alert('Service Booked Successfully!!!');window.location='/customer/book_service';</script>"

	return render_template('customer_book_service.html',data=data)
@customer.route('/service_bookings',methods=['get','post'])
def service_bookings():
	data={}
	q="select * from service_booking inner join service using(service_id) where customer_id='%s'"%(session['customer_id'])
	res=select(q)
	data['service_book']=res
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
		session['service_book_id']=id
	
	else:
		action=None
	if action=='payment':
		q="select * from customer inner join   cylinder_category using(cat_id) where customer_id='%s'"%(session['customer_id'])
		res=select(q)
		data['customer']=res
		q="select * from service_booking inner join service using(service_id)  where service_book_id='%s'"%(id)
		res=select(q)
		data['amount']=res
		session['amount']=res[0]['charge']

		return render_template('user_service_payment.html',data=data)
	return render_template('customer_view_service_booking.html',data=data)


@customer.route('/service_payment',methods=['get','post'])
def service_payment():
	q="insert into payment values(NULL,'%s','%s','service',curdate())"%(session['service_book_id'],session['amount'])
	insert(q)
	q="update service_booking set remarks='paid' where service_book_id='%s'"%(session['service_book_id'])
	update(q)
	return "<script>alert('Payment successfull!!!');window.location='/customer/customer_home';</script>"

