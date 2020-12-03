from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///post.db'
db=SQLAlchemy(app)

class BlogPost(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(100), nullable=False)
    content=db.Column(db.Text, nullable=False)
    author=db.Column(db.String(20), nullable=False, default='N/A')
    datePosted=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return 'Blog Post ' + str(self.id)

@app.route("/")
def func():
    return render_template('index.html')

@app.route("/posts", methods=['GET', 'POST'])
def posts():
    if request.method=="POST":
        pTitle=request.form['title']
        pContent=request.form['content']
        pAuthor=request.form['author']
        if pAuthor!='':
            post=BlogPost(title=pTitle, content=pContent, author=pAuthor)
        else:
            post=BlogPost(title=pTitle, content=pContent)
        db.session.add(post)
        try:
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()
        return redirect('/posts')
    else:
        allPosts=BlogPost.query.order_by(BlogPost.datePosted).all()
    return render_template('posts.html', posts=allPosts)

if __name__ == "__main__":
    app.run(debug=True)