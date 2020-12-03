from flask import Flask,render_template
app = Flask(__name__)

allPosts=[
    {
        "title": "post1",
        "content": "This is the content of post1",
        "author": "Aditya"
    },
    {
        "title": "post2",
        "content": "This is the content of post2"
    }
]

@app.route("/")
def func():
    return render_template('index.html')

@app.route("/posts")
def posts():
    return render_template('posts.html', posts=allPosts)

if __name__ == "__main__":
    app.run(debug=True)