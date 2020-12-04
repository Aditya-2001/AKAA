from flask import Flask,jsonify,render_template,request,redirect

app=Flask(__name__)

@app.route("/")
def home():
    return "WELCOME TO FLASK API"

employees=[
    {
        "id": 1,
        "Email": "aditya.iiita2001@gmail.com",
        "FirstName": "Aditya",
        "LastName": "Aggarwal",
        "Gender": "Male",
        "Profession": "Student",
        "Role": "N/A",
        "Contact": "(628) 464-8753x+91"
    },
    {
        "id": 2,
        "Email": "aditya@email.com",
        "FirstName": "Ad",
        "LastName": "Agg",
        "Gender": "Male",
        "Profession": "Student",
        "Role": "N/A",
        "Contact": "+91, press 2038138401803"
    }
]

@app.route("/employees",methods=['GET'])
def get():
    return jsonify({"employees": employees})

@app.route("/employees/<int:id>",methods=['GET'])
def getId(id):
    return jsonify({"employees": employees[id]})

@app.route("/employees",methods=['POST'])
def post():
    emp={
        "id": 3,
        "Email": "aditya@email.com",
        "FirstName": "Ad",
        "LastName": "Agg",
        "Gender": "Male",
        "Profession": "Student",
        "Role": "N/A",
        "Contact": "+91, press 2038138401803"
    }
    employees.append(emp)
    return jsonify({"created": employees})

@app.route("/employees/<int:id>",methods=['PUT'])
def put(id):
    employees[id]['Role']='XYZ'
    return jsonify({"updated": employees})

@app.route("/employees/<int:id>",methods=['DELETE'])
def delete(id):
    employees.remove(employees[id])
    return jsonify({"deleted": employees})

if __name__ == "__main__":
    app.run(debug=True)