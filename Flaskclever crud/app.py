from crypt import methods
from datetime import datetime
from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

#providing database
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///posts.db'

#creting db
db = SQLAlchemy(app)

#desing DB using class

class BlogPost(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(20), nullable=False, default='Unknown')
    date_posted = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)

    def __repr__(self):
        return 'Blog post '+str(self.id)


#dummy data for pass in html file


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts',methods=['GET','POST'])
def posts():

    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        post_author = request.form['author']
        new_post = BlogPost(title=post_title,content =post_content,author = post_author)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else:
        all_post = BlogPost.query.all()
        return render_template('post.html',posts = all_post)  # xyz.html, var_name =

@app.route('/posts/delete/<int:id>')
def delete(id):
    post = BlogPost.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/posts')

@app.route('/posts/edit/<int:id>',methods=['GET','POST'])
def edit(id):
    post = BlogPost.query.get_or_404(id)
    if request.method == 'POST':
      post.title = request.form['title']
      post.content = request.form['content']
      post.author = request.form['author']
      db.session.commit()
      return redirect('/posts')
    else:
      return render_template('edit.html',post = post)

if __name__ == "__main__":
    app.run(debug=True)