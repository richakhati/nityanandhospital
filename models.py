import settings


############# HOME SECTION STARTS ###############

class Home(settings.db.Model):
    id= settings.db.Column(settings.db.Integer, primary_key= True)
    home_text= settings.db.Column(settings.db.String)
    home_title= settings.db.Column(settings.db.String)
    home_img= settings.db.Column(settings.db.String)

############ HOME SECTION ENDS ####################

################ SLIDER STARTS ########################

class Slider(settings.db.Model):
    id= settings.db.Column(settings.db.Integer, primary_key= True)
    slider_image= settings.db.Column(settings.db.String)
    

################# SLIDER ENDS ##########################

################ ABOUT US START #########################

class Aboutus(settings.db.Model):
    id= settings.db.Column(settings.db.Integer, primary_key=True)
    file_au= settings.db.Column(settings.db.String)
    text_au= settings.db.Column(settings.db.String)
    title= settings.db.Column(settings.db.String)
    
################# ABOUT US END HERE ########################


################## DEPARTMENTS SECTION STARTS ###################

class Departments(settings.db.Model):
    id= settings.db.Column(settings.db.Integer, primary_key= True)
    dept_text= settings.db.Column(settings.db.String)
    dept_img= settings.db.Column(settings.db.String)
    dept_title= settings.db.Column(settings.db.String)

################## DEPARTMENTS SECTION END HERE ######################

################# SERVICES STARTS HERE ##################

class Service(settings.db.Model):
    id= settings.db.Column(settings.db.Integer, primary_key=True)
    serv_title= settings.db.Column(settings.db.String)
    serv_img=settings.db.Column(settings.db.String)
    serv_text= settings.db.Column(settings.db.String)
################ SERVICES ENDS HERE #####################

################### KNOW YOUR DOCTOR STARTS HERE ####################

class Docdetails(settings.db.Model):
    id = settings.db.Column(settings.db.Integer, primary_key= True)
    doc_name= settings.db.Column(settings.db.String)
    doc_title= settings.db.Column(settings.db.String)
    doc_img= settings.db.Column(settings.db.String)
    doc_text= settings.db.Column(settings.db.String)

#################### KNOW YOUR DOCTORS ENDS HERE #######################

################### PATIENT SERVICE STARTS HERE #####################

class Pservices(settings.db.Model):
    id = settings.db.Column(settings.db.Integer, primary_key= True)
    serv_title= settings.db.Column(settings.db.String)
    text= settings.db.Column(settings.db.String)
    img= settings.db.Column(settings.db.String)

################### PATIENT SERVICES ENDS ###########################

################# HEALTH EDUCATION #########################

class Healthedu(settings.db.Model):
    id= settings.db.Column(settings.db.Integer, primary_key= True)
    title = settings.db.Column(settings.db.String)
    text= settings.db.Column(settings.db.String)

################# HEALTH EDUCATION ENDS #########################

################ CONTACT US STARTS ####################

class Contactus(settings.db.Model):
    id= settings.db.Column(settings.db.Integer, primary_key= True)
    img= settings.db.Column(settings.db.String)
    con_title= settings.db.Column(settings.db.String)
    con_map= settings.db.Column(settings.db.String)
    query_num= settings.db.Column(settings.db.Integer)
    link= settings.db.Column(settings.db.String)
    name= settings.db.Column(settings.db.String)
    email= settings.db.Column(settings.db.String)
    message= settings.db.Column(settings.db.String)
    

################ CONTACT US ENDS  ####################

################ ADMIN ###############

class Admin(settings.db.Model):
    id = settings.db.Column(settings.db.Integer, primary_key= True)
    username= settings.db.Column(settings.db.String)
    password= settings.db.Column(settings.db.String)




