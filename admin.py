from flask import *
from database import *
admin=Blueprint('admin',__name__)

@admin.route('/admin_home',methods=['get','post'])
def admin_home():
	return render_template('admin_home.html')

@admin.route('/view_user',methods=['get','post'])
def view_user():
	data={}
	q="select * from customer inner join cylinder_category using(cat_id) inner join login using(username) where usertype='customer' "
	res=select(q)
	data['users']=res
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']		
	else:
		action=None

	if action=='install':
		q="update customer set install_status='installed' where customer_id='%s'"%(id)
		update(q)
		return redirect(url_for('admin.view_user'))

	return render_template('admin_view_users.html',data=data)

@admin.route('/manage_staff',methods=['get','post'])
def manage_staff():
	data={}
	
	if 'submit' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		hname=request.form['hname']
		dob=request.form['dob']
		city=request.form['city']
		district=request.form['district']
		state=request.form['state']
		pincode=request.form['pincode']
		email=request.form['email']
		phone=request.form['phone']
		description=request.form['description']
		password=request.form['password']
		q="select * from login where username='%s'"%(email)
		res=select(q)
		if res:
			return "<script>alert('email already exist!!!');window.location='manage_staff';</script>"
		else:
			q="insert into login values('%s','%s','staff')"%(email,password)
			insert(q)
			q="insert into staff values(NULL,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',now(),'approved')"%(email,fname,lname,dob,hname,city,district,state,pincode,phone,description)
			insert(q)
			return redirect(url_for('admin.manage_staff'))

	q="select * from staff WHERE `s_status` !='removed'"
	res=select(q)
	data['staffs']=res
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']

	else:
		action=None
	if action=='delete':
		q="select * from staff where staff_id='%s'"%(id)
		res=select(q)
		data['del']=res
		q="update staff set s_status='removed' where staff_id='%s'"%(id)
		update(q)
		q="update login set usertype='removed' where username='%s'"%(res[0]['username'])
		delete(q)
		return redirect(url_for('admin.manage_staff'))
	if action=='update':
		q="select * from staff where staff_id='%s'"%(id)
		res=select(q)
		data['updater']=res
	if 'update' in request.form:
		hname=request.form['hname']
		city=request.form['city']
		district=request.form['district']
		state=request.form['state']
		description=request.form['description']
		pincode=request.form['pincode']
		phone=request.form['phone']
		description=request.form['description']
		q="update staff set staff_hname='%s',staff_city='%s',staff_district='%s',staff_state='%s',staff_des='%s',staff_pincode='%s',staff_phno='%s' where staff_id='%s'"%(hname,city,district,state,description,pincode,phone,id)
		update(q)
		return redirect(url_for('admin.manage_staff'))
	return render_template('admin_manage_staffs.html',data=data)

@admin.route('/manage_category',methods=['get','post'])
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
		return redirect(url_for('admin.manage_category'))
	q="select * from cylinder_category"
	res=select(q)
	data['category']=res
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
		q2="SELECT SUM(no_of_cylin) as TOTAL FROM stock WHERE `cat_id`='%s'"%(id)
		total=select(q2)
		#print(total)
		data['total']=total
	else:
		action=None
	if action=='delete':
		q="delete from cylinder_category where cat_id='%s'"%(id)
		delete(q)
		return redirect(url_for('admin.manage_category'))
	if action=='update':
		q="select * from cylinder_category where cat_id='%s'"%(id)
		res=select(q)
		data['updater']=res
	if 'update' in request.form:
		price=request.form['price']
		q="update cylinder_category set price='%s' where cat_id='%s'"%(price,id)
		update(q)
		return redirect(url_for('admin.manage_category'))
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
		return redirect(url_for('admin.manage_category',action='stock',id=id))
	return render_template('admin_manage_category.html',data=data)

@admin.route('/manage_service',methods=['get','post'])
def manage_service():
	data={}

	if 'submit' in request.form:
		service_type=request.form['service']
		price=request.form['price']
	
		q="insert into service values(NULL,'%s','%s')"%(service_type,price)
		insert(q)
		return redirect(url_for('admin.manage_service'))
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
		return redirect(url_for('admin.manage_service'))
	if action=='update':
		q="select * from service where service_id='%s'"%(id)
		res=select(q)
		data['updater']=res
	if 'update' in request.form:
		price=request.form['price']
		q="update service set charge='%s' where service_id='%s'"%(price,id)
		update(q)
		return redirect(url_for('admin.manage_service'))
	return render_template('admin_manage_service.html',data=data)

@admin.route('/manage_vehicles',methods=['get','post'])
def manage_vehicles():
	data={}
	if 'submit' in request.form:
		reg_no=request.form['reg_no']
		vehicle_type=request.form['vehicle_type']
	
		q="insert into vehicle values('%s','%s','free','approved')"%(reg_no,vehicle_type)
		insert(q)
		return redirect(url_for('admin.manage_vehicles'))
	q="select * from vehicle WHERE `V_Status` !='removed' "
	res=select(q)
	data['vehicle']=res
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	
	else:
		action=None
	if action=='delete':
	
		q="update vehicle set V_Status='removed' where vehicle_regno='%s'"%(id)
		update(q)
		return redirect(url_for('admin.manage_vehicles'))
	return render_template('admin_manage_vehicles.html',data=data)


@admin.route('/new_connection_request',methods=['get','post'])
def new_connection_request ():
    q = "select * from customer inner join cylinder_category using(cat_id) inner join login using(username) where usertype='pending' "
    res = select (q)
    data['users'] = res
    if 'action' in request.args:
        action = request.args['action']
        id = request.args['id']
    else:
        action = None
    if action == 'accept':
        q = "update login set usertype='customer' where username='%s'" % (id)
        update (q)
        q1 = "update customer set c_status='approved' where username='%s'" % (id)
        update (q1)
        return redirect (url_for ('admin.view_user'))
    if 'submit' in request.form:
        q = "select * from customer where customer_id='%s'" % (id)
        res = select (q)
        charge = request.form['charge']
        q = "update login set usertype='customer' where username='%s'" %(res[0]['username'])
        update (q)
        q =	"update customer set c_status='approved',delivery_charge='%s' where customer_id='%s'"% (charge,id)
        update (q)
    return redirect (url_for ('admin.new_connection_request'))
    if action == 'reject':
        q ="update login set usertype='rejected' where username='%s'" %(id)
        update (q)
        q ="update customer set c_status='rejected' where username='%s'" %(id) 
        update (q) 
        return redirect (url_for ('admin.view_user')) 
    return render_template ('admin_view_new_connection_request.html',data = data)

@admin.route('/view_booking',methods=['get','post'])
def view_booking():
	data={}
	q="select * from booking inner join customer using(customer_id)inner join cylinder_category using(cat_id)"
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
		return redirect(url_for('admin.view_booking'))
	if action=="assign":
		q="select * from vehicle where V_Status='approved'"
		res=select(q)
		data['vehicles']=res
		q1="select * from staff where s_status='approved'"
		res1=select(q1)
		data['staff']=res1
		q="select * from booking inner join customer using(customer_id) where book_id='%s'"%(id)
		res=select(q)
		data['book']=res
	if action=="deliver":
		q="update booking set status='delivered' where book_id='%s'"%(id)
		update(q)
		q="update delivery set delivery_status='delivered' where book_id='%s'"%(id)
		update(q)
		return redirect(url_for('admin.view_booking'))
	if 'submit' in request.form: 	
		vehicle_id=request.form['vehicle_id']
		q="insert into delivery values(NULL,'%s','%s',curdate(),'out for delivery')"%(id,vehicle_id)
		insert(q)
		q="update booking set status='vehicle_assigned' where book_id='%s'"%(id)
		update(q)

		return redirect(url_for('admin.view_booking'))
	return render_template('admin_view_booking.html',data=data)

@admin.route('/view_complaints',methods=['get','post'])
def view_complaints():
	data={}
	q="select * from complaint inner join customer using(customer_id)"
	res=select(q)
	data['complaints']=res
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
		session['cid']=id
	else:
		action=None
	if action=='reply':
		q="select * from complaint inner join customer using(customer_id) where complaint_id='%s'"%(id)
		res=select(q)
		data['complaint']=res
		return render_template('admin_send_reply.html',data=data)
	return render_template('admin_view_complaints.html',data=data)

@admin.route('/reply_complaints',methods=['get','post'])
def reply_complaints():
	reply=request.form['reply']
	q="update complaint set reply='%s' where complaint_id='%s'"%(reply,session['cid']) 
	update(q)
	return redirect(url_for('admin.view_complaints'))


@admin.route('/view_service_booking',methods=['get','post'])
def view_service_booking():
	data={}
	q="select * from service_booking inner join customer using(customer_id) inner join service using(service_id)"
	res=select(q)
	data['service_bookings']=res
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
		q="update service_booking set remarks ='approved' where service_book_id ='%s'"%(id)
		res=update(q)
		q="select * from service_booking INNER JOIN customer USING(customer_id) INNER JOIN service USING(service_id) where service_book_id='%s'"%(id)
		res=select(q)
		data['ser']=res
		q="insert "

	if action=='reject':
		q="update service_booking set remarks ='rejected' where service_book_id ='%s'"%(id)
		res=update(q)
	return render_template('admin_view_service_booking.html',data=data)

@admin.route('/view_service_report',methods=['get','post'])
def view_servivce_report():
	data={}
	q="SELECT * FROM cus_service INNER JOIN service_booking USING(service_book_id) INNER JOIN staff USING(staff_id) INNER JOIN service USING(service_id)INNER JOIN customer USING(customer_id) INNER JOIN cylinder_category USING(cat_id) "
	res=select(q)
	data['service_report']=res
	return render_template('admin_view_service_report.html',data=data)

@admin.route('/view_booking_report',methods=['get','post'])
def view_booking_report():
	data={}
	q="SELECT * FROM `delivery` INNER JOIN booking USING(book_id) INNER JOIN customer USING(customer_id) INNER JOIN cylinder_category USING(cat_id) INNER JOIN vehicle USING(vehicle_regno)"
	res=select(q)
	data['booking_report']=res
	return render_template('admin_view_booking_report.html',data=data)

@admin.route('/view_staff_report',methods=['get','post'])
def view_staff_report():
	data={}
	q="SELECT * FROM `staff`"
	res=select(q)
	data['staff_report']=res
	return render_template('admin_view_staff_report.html',data=data)


