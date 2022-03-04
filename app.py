from json.tool import main
import string
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello world"

# @app.route('/home')   #it will run hello fun for /home  
# @app.route('/home/<string:name>')  #we can passthe variable from url and use it function expmple like for various image that hve different url then we can use it's id for show
# #dynamic url

# @app.route('/home/user/<string:name>/post/<int:id>')
# def hello(name,id):
#     return "hello " +name+" your id :"+str(id)

@app.route('/onlyget', methods = ['GET','POST'])
def get_req():
    return "you can only get this"
if __name__=="__main__":
    app.run(debug=True) 