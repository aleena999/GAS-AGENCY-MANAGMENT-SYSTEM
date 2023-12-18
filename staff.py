from flask import *
from database import *
staff=Blueprint('staff',__name__)
@staff.route('/staffhome')
def staffhome():
	return render_template('staff_home.html')

@staff.route('/manage_category',methods=['get','post'])
def manage_category():
	data={}
	if 'submit' in request.form:
		category=request.form['category']
		price=request.form['price']
	
		q="insert into cylinder_category values(NULL,'%s','%s')"%(category,price)
		cid=insert(q)
		q="insert into stock values(NULL,curdate(),'Full','%s',0)"%(cid)
		insert(q)
		q="insert into stock values(NULL,curdate(),'Empty','%s',0)"%(cid)
		insert(q)
		q="insert into stock values(NULL,curdate(),'Damaged','%s',0)"%(cid)
		insert(q)

		return redirect(url_for('staff.manage_category'))
	q="select * from cylinder_category"
	res=select(q)
	data['category']=res
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	
	else:
		action=None
	if action=='delete':
	
		q="delete from cylinder_category where cat_id='%s'"%(id)
		delete(q)
		return redirect(url_for('staff.manage_category'))
	if action=='update':
		q="select * from cylinder_category where cat_id='%s'"%(id)
		res=select(q)
		data['updater']=res
	if 'update' in request.form:
		price=request.form['price']
		q="update cylinder_category set price='%s' where cat_id='%s'"%(price,id)
		update(q)
		return redirect(url_for('staff.manage_category'))
	if action=="stock":
		q="select * from cylinder_category where cat_id='%s'"%(id)
		res=select(q)
		data['stock']=res
		q="select * from stock where cat_id='%s'"%(id)
		res=select(q)
		data['stocks']=res
	if 'stock' in request.form:
		stock=request.form['stock']
		stock_type=request.form['stock_type']
		q="update stock set no_of_cylin=no_of_cylin+'%s',stock_date=curdate() where stock_type='%s' and cat_id='%s'"%(stock,stock_type,id)
		update(q)
		return redirect(url_for('staff.manage_category',action='stock',id=id))
	return render_template('staff_manage_category.html',data=data)


@staff.route('/manage_service',methods=['get','post'])
def manage_service():
	data={}

	if 'submit' in request.form:
		service_type=request.form['service']
		price=request.form['price']
	
		q="insert into service values(NULL,'%s','%s')"%(service_type,price)
		insert(q)
		return redirect(url_for('staff.manage_service'))
	q="select * from service"
	res=select(q)
	data['service']=res
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	
	else:
		action=None
	if action=='delete':
	
		q="delete from service where service_id='%s'"%(id)
		delete(q)
		return redirect(url_for('staff.manage_service'))
	if action=='update':
		q="select * from service where service_id='%s'"%(id)
		res=select(q)
		data['updater']=res
	if 'update' in request.form:
		price=request.form['price']
		q="update service set charge='%s' where service_id='%s'"%(price,id)
		update(q)
		return redirect(url_for('staff.manage_service'))
	return render_template('staff_manage_service.html',data=data)

@staff.route('/manage_vehicles',methods=['get','post'])
def manage_vehicles():
	data={}
	if 'submit' in request.form:
		reg_no=request.form['reg_no']
		vehicle_type=request.form['vehicle_type']
	
		q="insert into vehicle values('%s','%s','free','approved')"%(reg_no,vehicle_type)
		insert(q)
		return redirect(url_for('staff.manage_vehicles'))
	q="select * from vehicle"
	res=select(q)
	data['vehicle']=res
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	
	else:
		action=None
	if action=='delete':
	
		q="Update vehicle set V_Status='removed' where vehicle_regno='%s'"%(id)
		update(q)
		return redirect(url_for('staff.manage_vehicles'))
	if action=='update':
		q="select * from vehicle where vehicle_regno='%s'"%(id)
		res=select(q)
		data['updater']=res
		return redirect(url_for('staff.manage_vehicles'))
	return render_template('staff_manage_vehicles.html',data=data)

@staff.route('/view_user',methods=['get','post'])
def view_user():
	data={}
	q="select * from customer inner join cylinder_category using(cat_id) inner join login using(username) where usertype='customer' "
	res=select(q)
	data['users']=res

	return render_template('staff_view_users.html',data=data)
@staff.route('/new_connection_request',methods=['get','post'])
def new_connection_request():
	
	data={}
	q="select * from customer inner join cylinder_category using(cat_id) inner join login using(username) where usertype='pending' "
	res=select(q)
	data['users']=res
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	
	else:
		action=None
	if action=='accept':
		q="update login set usertype='customer' where username='%s'"%(id)
		update(q)
		q1="update customer set c_status='approved' where username='%s'"%(id)
		update(q1)
		return redirect(url_for('staff.new_connection_request'))
	if action=='reject':
		q="update login set usertype='rejected' where username='%s'"%(id)
		update(q)
		q="update customer set c_status='rejected' where username='%s'"%(id)
		update(q)
		return redirect(url_for('staff.new_connection_request'))
	return render_template('staff_view_new_connection_request.html',data=data)


@staff.route('/view_booking',methods=['get','post'])
def view_booking():
	data={}
	q="select * from booking inner join customer using(customer_id)inner join cylinder_category using(cat_id) "
	res=select(q)
	data['booking']=res
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	
	else:
		action=None
	if action=='payment':
		q="select * from payment where booked_id='%s' and type='booking'"%(id)
		res=select(q)
		data['payment']=res
	if action=='accept':
		q="update booking set status='approved' where book_id='%s'"%(id)
		update(q)
		q="select * from booking where book_id='%s'"%(id)
		res=select(q)
		data['book']=res
		q="update customer set cylin_inhand=cylin_inhand+'%s' where customer_id='%s'"%(1,data['book'][0]['customer_id'])
		update(q)
		return redirect(url_for('staff.view_booking'))
	if action=="assign":
		q="select * from vehicle"
		res=select(q)
		data['vehicles']=res
		q="select * from booking inner join customer using(customer_id) where book_id='%s'"%(id)
		res=select(q)
		data['book']=res
	if action=="deliver":
		q="update booking set status='DELIVERED' where book_id='%s'"%(id)
		update(q)
		return redirect(url_for('staff.view_booking'))
	if 'submit' in request.form: 	
		vehicle_id=request.form['vehicle_id']
		q="insert into delivery values(NULL,'%s','%s',curdate(),'out for delivery')"%(id,vehicle_id)
		insert(q)
		q="update booking set status='vehicle_assigned' where book_id='%s'"%(id)
		update(q)

		return redirect(url_for('staff.view_booking'))
		
	return render_template('staff_view_booking.html',data=data)


@staff.route('/view_service_booking',methods=['get','post'])
def view_service_booking():
	data={}
	q="select * from service_booking inner join customer using(customer_id) inner join service using(service_id) inner join cylinder_category using(cat_id)"
	res=select(q)
	data['services']=res
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	
	else:
		action=None
	if action=='payment':
		q="select * from payment where booked_id='%s' and type='service'"%(id)
		res=select(q)
		data['payment']=res
	if action=='accept':
		q="select * from service_booking inner join service using(service_id) inner join customer using(customer_id) where service_book_id='%s'"%(id)
		res=select(q)
		data['ser']=res
	if 'submit' in request.form:
		remarks=request.form['remarks']
		q="insert into cus_service values(NULL,'%s','%s','%s',curdate())"%(id,session['staff_id'],remarks)
		insert(q)
		q="update service_booking set  remarks='accepted' where service_book_id='%s'"%(id)
		update(q)
		return redirect(url_for('staff.view_service_booking'))
	if action=="reject":
		q="update service_booking set  remarks='rejected' where service_book_id='%s'"%(id)
		update(q)
		return redirect(url_for('staff.view_service_booking'))

	return render_template('staff_view_service_booking.html',data=data)