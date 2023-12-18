from flask import *
from database import *
import uuid

public=Blueprint('public',__name__)
@public.route('/',methods=['get','post'])
def index():
    return render_template('index.html')

@public.route('/login',methods=['get','post'])
def login():
    if 'submit' in request.form:
        uname=request.form['username']
        pwd=request.form['password']
        q="select * from login where (username='%s' and password='%s')"%(uname,pwd)
        res=select(q)
        if res:
            session['username']=res[0]['username']
            if res[0]['usertype']=="admin":
                return redirect(url_for('admin.admin_home'))
            if res[0]['usertype']=="staff":
                q="select * from staff where username='%s'"%(session['username'])
                res=select(q)
                session['staff_id']=res[0]['staff_id']
                return redirect(url_for('staff.staffhome'))
            if res[0]['usertype']=="customer":
                q="select * from customer where username='%s'"%(res[0]['username'])
                res=select(q)
                session['customer_id']=res[0]['customer_id']
                return redirect(url_for('customer.customer_home'))
            if res[0]['usertype']=='removed':
                return "<script>alert('CANNOT LOGIN!!!');window.location='/';</script>"
            if res[0]['usertype']=='pending':
                return "<script>alert('New Connection Request Pending!!!');window.location='/';</script>"


    return render_template('login.html')

@public.route('/register',methods=['get','post'])
def register():
    data={}
    q="select * from cylinder_category"
    res=select(q)
    data['cat']=res
    if 'submit' in request.form:
        email=request.form['email']
        q="select * from login where username='%s'"%(email)
        res=select(q)
        if res:
             return "<script>alert('email already exist!!!');window.location='/register';</script>"

        else:
        
            pwd=request.form['password']
            first_name=request.form['fname']
            last_name=request.form['lname']
            house_name=request.form['hname']
            email=request.form['email']
            phone=request.form['phone']
            city=request.form['city']
            district=request.form['district']
            state=request.form['state']
            pincode=request.form['pincode']
            proof_of_address=request.files['proof_of_address']
            path1='static/images/'+str(uuid.uuid4())+str(proof_of_address.filename)
            proof_of_address.save(path1)
            proof_of_identity=request.files['proof_of_identity']
            path2='static/images/'+str(uuid.uuid4())+str(proof_of_identity.filename)
            proof_of_identity.save(path2)
            adhar=request.form['adhar']
            cat_id=request.form['cat_id']
            connection_type=request.form['connection_type']
            q="insert into login(username,password,usertype)values('%s','%s','pending')"%(email,pwd)
            id=insert(q)
            q="insert into customer (username,adhaar_no,cus_fname,cus_lname,cus_hname,cus_city,cus_district,cus_state,pincode,cus_phno,c_status,proof_of_address,proof_of_identity,cat_id,connection_type,delivery_charge,cylin_inhand,install_status) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','pending','%s','%s','%s','%s','0','0','pending')"%(email,adhar,first_name,last_name,house_name,city,district,state,pincode,phone,path1,path2,cat_id,connection_type)
            insert(q)
    return render_template('register.html',data=data)