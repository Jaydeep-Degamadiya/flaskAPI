
from flask import Flask,render_template

app = Flask(__name__)

#dummy data for pass in html file
all_post = [

    {
        'title' : 'post 1',
        'desc' : 'This the the first post',
        'author' : 'JD'
    },
     {
        'title' : 'post 2',
        'desc' : 'This the the second post'
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts')
def posts():
    return render_template('post.html',posts = all_post)  # xyz.html, var_name =

if __name__ == "__main__":
    app.run(debug=True)