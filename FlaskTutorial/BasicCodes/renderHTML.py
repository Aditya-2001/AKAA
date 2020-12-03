from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def func():
    return render_template('index.html')
@app.route('/home/<string:name>')
def hello(name):
    return "Hello " + name

@app.route("/onlyget", methods=["GET"])
def func1():
    return "Only post methods are allowed"

if __name__ == "__main__":
    app.run(debug=True)