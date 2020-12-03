from flask import Flask
app = Flask(__name__)

@app.route('/home/<string:name>')
def hello(name):
    return "Hello " + name

@app.route("/onlyget", methods=["GET"])
def func():
    return "Only post methods are allowed"

if __name__ == "__main__":
    app.run(debug=True)