from flask import Flask,render_template,request,redirect,jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from marshmallow import Schema, fields, ValidationError, pre_load

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///post.db'
db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    Email=db.Column(db.String(30), nullable=False)
    FirstName=db.Column(db.String(50), nullable=False)
    LastName=db.Column(db.String(50), nullable=False)
    Gender=db.Column(db.String(10), nullable=False)
    Profession=db.Column(db.String(50), nullable=False)
    Role=db.Column(db.String(50), nullable=False)
    Contact=db.Column(db.Integer, nullable=False)
    datePosted=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    def __repr__(self):
        return 'User ' + str(self.id)

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    Email=fields.Str()
    FirstName=fields.Str()
    LastName=fields.Str()
    Gender=fields.Str()
    Profession=fields.Str()
    Role=fields.Str()
    Contact=fields.Int()
    datePosted=fields.DateTime(dump_only=True)
    Name = fields.Method("format_name", dump_only=True)

    def format_name(self, author):
        return "{}, {}".format(author.FirstName, author.LastName)

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@app.route("/")
def func():
    return render_template('home.html')

@app.route("/user/signup",methods=['POST'])
def signup():
    if request.method=="POST":
        Email=request.form['email']
        fName=request.form['fName']
        lName=request.form['lName']
        Gender=request.form['gender']
        Profession=request.form['profession']
        Role=request.form['role']
        Contact=request.form['contact']
        post=User(Email=Email, FirstName=fName, LastName=lName, Gender=Gender, Profession=Profession, Role=Role, Contact=Contact)
        db.session.add(post)
        try:
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()
        return "User Added"
    else:
        return "Invalid request"

@app.route("/user/all")
def allusers():
    users=User.query.all()
    result=users_schema.dump(users)
    return {"Users": result}

if __name__=="__main__":
    app.run(debug=True)