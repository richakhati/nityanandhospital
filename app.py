import settings
from settings import app, db
import models 

@app.route('/admin', methods= ['GET', 'POST'])
def rids():
    if not settings.session.get('name'):
        return settings.redirect('/login')
    
    return settings.render_template('admin/index.html')

@app.route('/login', methods= ['GET', 'POST'])
def admin():
    if settings.request.method=='POST':
        if settings.request.form['uname']== '' or settings.request.form['password'] == "":
            return settings.redirect('/login')
        creds= models.Admin.query.filter_by(username= settings.request.form['uname'], password= settings.request.form['password'] )      
    
        if creds == None:
            return settings.redirect('/login')
        else:
            settings.session['name'] = settings.request.form['uname']
            return settings.redirect('/admin')

    return settings.render_template('admin/login.html')

########################## HOME ######################################





########################### HOME SLIDER #########################################

@app.route('/homeslider', methods=['GET', 'POST'])
def home():
    if settings.request.method== 'POST':
        slider_image= settings.request.files['slider_image']
       
        fname= 'static/admin-assets/img/nnh/'+settings.secure_filename(slider_image.filename)
        slider_image.save(fname)
        info= models.Slider(slider_image=fname)
        settings.db.session.add(info)
        settings.db.session.commit()

    fetchslider= models.Slider.query.all()
    return settings.render_template('admin/homeslider.html', fetchslider=fetchslider)

@app.route('/deleteslider')
def slidelte():
    id= settings.request.args['id']
    fetchslider= models.Slider.query.filter_by(id=id).first()
    db.session.delete(fetchslider)
    db.session.commit()
    return settings.redirect ('/homeslider')


########################### HOME SLIDER ENDS #############################

############################ DOCTORS STARTS ###############################
@app.route('/docadd', methods= ['GET', 'POST'])
def add():
    if settings.request.method=='POST':
      doc_title  = settings.request.form['doc_title']
      doc_name= settings.request.form['doc_name']
      doc_text= settings.request.form['ckeditor']
      doc_img = settings.request.files['doc_img']
      fname= 'static/admin-assets/img/nnh/'+settings.secure_filename(doc_img.filename)
      doc_img.save(fname)
      info= models.Docdetails(doc_title= doc_title, doc_name= doc_name, doc_text= doc_text, doc_img=fname)
      settings.db.session.add(info)
      settings.db.session.commit()

    fetch= models.Docdetails.query.all()
    return settings.render_template('admin/docadd.html', getinfo= fetch)

@app.route('/docedit', methods=['GET', 'POST'])
def edit():

    if settings.request.method=='POST':
      doc_title  = settings.request.form['doc_title']
      doc_name= settings.request.form['doc_name']
      doc_text= settings.request.form['ckeditor']
      doc_img = settings.request.files['doc_img']
      fname= 'static/admin-assets/img/nnh/'+settings.secure_filename(doc_img.filename)
      doc_img.save(fname)
      id= settings.request.form['id']
      fetch= models.Docdetails.query.filter_by(id=id).first()
      fetch.doc_title=doc_title
      fetch.doc_name=doc_name
      fetch.doc_text=doc_text
      fetch.doc_img=fname
      settings.db.session.commit()
      return settings.redirect('/docadd')

    id= settings.request.args['id']
    fetchdetails= models.Docdetails.query.filter_by(id=id).first()
    fetchall= models.Docdetails.query.all()
    return settings.render_template('admin/docedit.html', getinfo= fetchdetails,fetchall=fetchall)

################################# DOCTOR ENDS HERE ################################ 

################################ SERVVICES ENDS #################################
    
@app.route('/service', methods=['GET', 'POST'])
def serv():
    if settings.request.method=='POST':
        serv_title= settings.request.form['serv_title']
        serv_text= settings.request.form['ckeditor']
        serv_img= settings.request.files['serv_img']
        fname= 'static/admin-assets/img/nnh/'+settings.secure_filename(serv_img.filename)
        serv_img.save(fname)
        serv= models.Service(serv_title=serv_title, serv_text=serv_text, serv_img=fname)
        settings.db.session.add(serv)
        settings.db.session.commit()

    fetchserv= models.Service.query.all()
    return settings.render_template('admin/service.html', fetchserv=fetchserv)

@app.route('/servedit', methods=['GET', 'POST'])
def serve():
    if settings.request.method=='POST':
        serv_title= settings.request.form['serv_title']
        serv_text= settings.request.form['ckeditor']
        serv_img= settings.request.files['serv_img']
        fname= 'static/admin-assets/img/nnh/'+settings.secure_filename(serv_img.filename)
        serv_img.save(fname)
        id= settings.request.form['id']
        fetch= models.Service.query.filter_by(id=id).first()
        fetch.serv_title=serv_title
        fetch.serv_text=serv_text
        fetch.serv_img=fname
        settings.db.session.commit()
        return settings.redirect('/service')

    id= settings.request.args['id']
    fetch1= models.Service.query.filter_by(id=id).first()
    fetch= models.Service.query.all()
    return settings.render_template('admin/servedit.html', fetch=fetch,fetch1=fetch1)

########################## SERVICES ENDS ##########################

######################### DEPARTMENTS STARTS ######################

@app.route('/dept', methods= ['GET', 'POST'])
def dep():
    if settings.request.method=="POST":
        dept_text= settings.request.form['ckeditor']
        dept_img= settings.request.files['dept_img']
        fname= 'static/admin-assets/img/nnh/'+settings.secure_filename(dept_img.filename)
        dept_img.save(fname)
        dept_title= settings.request.form['dept_title']
        dep= models.Departments(dept_text=dept_text, dept_img=fname, dept_title= dept_title)
        settings.db.session.add(dep)
        settings.db.session.commit()

    fetchdep= models.Departments.query.all()
    return settings.render_template('admin/dept.html', fetchdep=fetchdep)

@app.route('/deptedit', methods=['GET', 'POST'])
def depted():
    if settings.request.method=='POST':
        dept_text= settings.request.form['ckeditor']
        dept_img= settings.request.files['dept_img']
        fname= 'static/admin-assets/img/nnh/'+settings.secure_filename(dept_img.filename)
        dept_img.save(fname)
        dept_title= settings.request.form['dept_title']
        id= settings.request.form['id']
        fetchdep= models.Departments.query.filter_by(id=id).first()
        fetchdep.dept_text=dept_text
        fetchdep.dept_title=dept_title
        fetchdep.dept_img=fname
        settings.db.session.commit()
        return settings.redirect('/dept')

    id= settings.request.args['id']
    fetchdept= models.Departments.query.filter_by(id=id).first()
    fetchdep= models.Departments.query.all()
    return settings.render_template('admin/deptedit.html', fetchdept=fetchdept)

######################### DEPARTMENT ENDS HERE ########################

######################## PATIENT SERVICES STARTS HERE ######################
@app.route('/pservice', methods=['GET', 'POST'])
def patient():
    if settings.request.method=="POST":
        serv_title= settings.request.form['serv_title']
        text= settings.request.form['ckeditor']
        img= settings.request.files['img']
        fname= 'static/admin-assets/img/nnh/'+settings.secure_filename(img.filename)
        img.save(fname)
        patient=models.Pservices(serv_title=serv_title, text=text,img=fname)
        settings.db.session.add(patient)
        settings.db.session.commit()

    fetchpatient= models.Pservices.query.all()
    return settings.render_template('admin/pservice.html', fetchpatient=fetchpatient)

@app.route('/pservedit', methods=['GET', 'POST'])
def pedit():
    if settings.request.method=='POST':
        serv_title= settings.request.form['serv_title']
        text= settings.request.form['ckeditor']
        img= settings.request.files['img']
        fname= 'static/admin-assets/img/nnh/'+settings.secure_filename(img.filename)
        img.save(fname)
        id= settings.request.form['id']
        fetchdep= models.Pservices.query.filter_by(id=id).first()
        fetchdep.text=text
        fetchdep.serv_title=serv_title
        fetchdep.img=fname
        settings.db.session.commit()
        return settings.redirect('/pservice')

    id= settings.request.args['id']
    fetchpat= models.Pservices.query.filter_by(id=id).first()
    fetchpatient= models.Pservices.query.all()
    return settings.render_template('admin/pservedit.html', fetchpat=fetchpat) 

            ##############BILLING ENDS###############

        ################## Make An Appointment- SMTP Starts ###############

@app.route('/email' ,methods= ['GET', 'POST'])
def mail():
    if settings.request.method=='POST':
        name= settings.request.form['name']
        mail= settings.request.form['mail']
        phone= settings.request.form['phone']
        doctor= settings.request.form['doctor']
        date= settings.request.form['date']
        subject= settings.request.form['subject']
        
        msg  = settings.Message('Hello', sender = app.config['MAIL_USERNAME'], recipients =['riiichakhati18@gmail.com'])
        msg.body = "Name: "+ name + "\nEmail: "+ mail +"\nDate of appointment: "+ date + "\nYour Phone no.: "+ phone+ "\nSelect Your Doctor :" + doctor + "\nYour subject" + subject
        
        settings.mail.send(msg)
        
    fetch= models.Docdetails.query.all()
    return settings.render_template('fe/email.html', fetch=fetch)

        ################### Make An Appointment- SMTP ENDS ###################

######################### VISITORS RIGHTS AND RESPONSIBILITIES #############################
@app.route('/vresp', methods=['GET','POST'])
def visitor():
    if settings.request.method=='POST':
        image= settings.request.files['image']
        fname= 'static/admin-assets/img/nnh/'+settings.secure_filename(image.filename)
        image.save(fname)
        serv_title= settings.request.form['serv_title']
        visit= models.Pservices(img=fname, serv_title=serv_title)
        settings.db.session.add(visit)
        settings.db.session.commit()

    fetch= models.Pservices.query.all()
    return settings.render_template('admin/vresp.html', fetch=fetch)

@app.route('/delete')
def vresp():
    id= settings.request.args['id']
    fetch= models.Pservices.query.filter_by(id=id).first()
    db.session.delete(fetch)
    db.session.commit()
    return settings.redirect ('/vresp')





######################## HEALTH EDUCATION #######################
@app.route('/health', methods=['GET', 'POST'])
def edu():
    if settings.request.method=="POST":
        title= settings.request.form['title']
        text= settings.request.form['ckeditor']
        edu= models.Healthedu(title=title, text=text)
        settings.db.session.add(edu)
        settings.db.session.commit()

    fetchedu= models.Healthedu.query.all()
    return settings.render_template('admin/health.html', fetchedu=fetchedu)

@app.route('/healthedit', methods=['GET', 'POST'])
def educat():
    if settings.request.method=='POST':
        text= settings.request.form['ckeditor']
        title= settings.request.form['title']
        id= settings.request.form['id']
        fetched= models.Healthedu.query.filter_by(id=id).first()
        fetched.text=text
        fetched.title=title
        settings.db.session.commit()
        return settings.redirect('/health')

    id= settings.request.args['id']
    fetched= models.Healthedu.query.filter_by(id=id).first()
    fetchedu= models.Healthedu.query.all()
    return settings.render_template('admin/healthedu.html', fetched=fetched, fetchedu=fetchedu)


########################### ABOUT STARTS ###########################

@app.route('/about', methods= ['GET', 'POST'])
def abt():
    if settings.request.method=='POST': 
        title= settings.request.form['title']
        text= settings.request.form['ckeditor']
        file = settings.request.files['file']
        fname= 'static/admin-assets/img/nnh/'+settings.secure_filename(file.filename)
        file.save(fname)
        id= settings.request.form['id']
        fetch= models.Aboutus.query.filter_by(id=id).first()
        fetch.title=title
        fetch.file_au=fname
        fetch.text_au=text
        fetch.file=fname
        settings.db.session.commit()
        return settings.redirect('/about?id=1')

    id= settings.request.args['id']
    fetch=models.Aboutus.query.filter_by(id=id).first()
    fetchabout= models.Aboutus.query.all()

    return settings.render_template('admin/aboutus.html', fetch=fetch, fetchabout=fetchabout    )


############################# ABOUT ENDS ###########################

############################ CONTACT US ##########################
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if settings.request.method=='POST':
        img= settings.request.files['img']
        fname=  'static/admin-assets/img/nnh/'+settings.secure_filename(img.filename)
        img.save(fname)
        con_title= settings.request.form['con_title']
        con_num= settings.request.form['con_num']
        con_add= settings.request.form['con_add']
        query_num= settings.request.form['query_num']
        time= settings.request.form['time']
        info= models.Contactus(img=fname, con_num=con_num, con_add=con_add, query_num=query_num, time=time, con_title=con_title)
        settings.db.session.add(info)
        settings.db.session.commit()

    fetchcon= models.Contactus.query.all()
    return settings.render_template('admin/contact.html', fetchcon=fetchcon)

@app.route('/contactedit', methods=['GET', 'POST'])
def editcon():
    if settings.request.method=='POST':
        img= settings.request.files['img']
        fname=  'static/admin-assets/img/nnh/'+settings.secure_filename(img.filename)
        img.save(fname)
        con_title= settings.request.form['con_title']
        con_num= settings.request.form['con_num']
        con_add= settings.request.form['con_add']
        query_num= settings.request.form['query_num']
        time= settings.request.form['time']
        id= settings.request.form['id']
        fetchcontact= models.Contactus.query.filter_by(id=id).first()
        fetchcontact.con_title=con_title
        fetchcontact.con_num=con_num
        fetchcontact.con_add=con_add
        fetchcontact.query_num=query_num
        fetchcontact.time=time
        fetchcontact.img=fname
        settings.db.session.commit()
        return settings.redirect('/contact')

    id= settings.request.args['id']
    fetchcontact= models.Contactus.query.filter_by(id=id).first()
    fetchcon= models.Contactus.query.all()
    return settings.render_template('admin/contactedit.html', fetchcontact=fetchcontact, fetchcon=fetchcon)

@app.route('/direction', methods=['GET', 'POST'])
def direct():
    if settings.request.method=='POST':
        link= settings.request.form['link']        
        id= settings.request.form['id']
        fetchmap= models.Contactus.query.filter_by(id=id).first()
        fetchmap.link=link
        
        settings.db.session.commit()
        return settings.redirect('/direction')

    
    fetchmap=  models.Contactus.query.filter_by(id=1).first()
    return settings.render_template('admin/direction.html', fetchmap=fetchmap)

if __name__== '__main__':
    app.run(debug=True)