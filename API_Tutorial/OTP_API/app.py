from flask import *  
from flask_mail import *  
from random import *  
import clx.xms
import requests

app = Flask(__name__)  

mail = Mail(app)  
app.config["MAIL_SERVER"]='smtp.gmail.com'  
app.config["MAIL_PORT"] = 465      
app.config["MAIL_USERNAME"] = '#'  
app.config['MAIL_PASSWORD'] = '#'  
app.config['MAIL_USE_TLS'] = False  
app.config['MAIL_USE_SSL'] = True  

mail = Mail(app)     

@app.route('/')  
def index():  
    return render_template("home.html")  

@app.route('/verifyEmail',methods = ["POST"])  
def verifyEmail():  
    email = request.form["email"]   
    otp = randint(000000,999999)
    msg = Message('OTP',sender = '#', recipients = [email])  
    msg.body = "OTP For email verification is: " + str(otp)  
    mail.send(msg)  
    return render_template('verifyOTP.html', Email=email, OTP=otp, Number="N/A")  

@app.route('/verifyPhone',methods = ["POST"])  
def verifyPhone():  
    phone = request.form["phone"]   
    otp = randint(000000,999999)
    sendOTPtoPhone(otp, str(phone))
    return render_template('verifyOTP.html', Email="N/A", OTP=otp, Number=phone) 

def sendOTPtoPhone(otp,number):
    client = clx.xms.Client(service_plan_id='#', token='#')
    create = clx.xms.api.MtBatchTextSmsCreate()
    create.sender = '#'
    SET={'a'}
    SET.pop()
    SET.add(number)
    create.recipients = SET
    create.body = 'OTP to verify phone number is: ' + str(otp)
    try:
        batch = client.create_batch(create)
    except (requests.exceptions.RequestException,
        clx.xms.exceptions.ApiException) as ex:
        print('Failed to communicate with XMS: %s' % str(ex)) 

@app.route('/validate',methods=["POST"])   
def validate(): 
    otp = request.form['originalOTP']
    email = request.form['email']
    contact = request.form['contact']
    user_otp = request.form['otp'] 
    if otp == user_otp:  
        if email=="N/A":
            return "<h3> " + contact + "  verification is  successful </h3>"  
        else:
            return "<h3> " + email + "  verification is  successful </h3>"  
    return "<h3>failure, OTP does not match</h3>"   

if __name__ == '__main__':  
    app.run(debug = True) 
