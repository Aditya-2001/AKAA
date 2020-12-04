# How to run API

Install flask: pip install flask
Running app.py: python app.py 
Run: http://127.0.0.1:5000/employees for GET request
To give POST request: curl -i -H "Content-Type: Application/json" -X POST http://localhost:5000/employees
To give PUT request: curl -i -H "Content-Type: Application/json" -X PUT http://localhost:5000/employees/id
To give DELETE request: curl -i -H "Content-Type: Application/json" -X DELETE http://localhost:5000/employees/id