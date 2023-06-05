from flask import Flask ,request, jsonify,abort
from pymongo import MongoClient
from model import User
from bson import json_util
  
app = Flask(__name__) #creating the Flask class object  
#app.config["MONGO_URI"] = "mongodb://localhost:27017/userdatabase"  #forming a connection with mongodb
client = MongoClient('localhost',27017) #basically creating an instance of mongodbclient class called client 
db = client['user_management_app'] #accessing the database

users = db['users']

@app.route('/hello')
def hello():
    return "Hello, World"
 
@app.route('/users', methods=['POST','GET']) #decorator drfines the   
def makeusers():
    if request.method=="POST":
        if not request.json:
            abort(400, 'Json is empty')
        name = request.json['name']
        email = request.json['email']
        user_signum= request.json['signum']
        new_user=User(signum=user_signum,name=name,email=email)
        
        users.insert_one(new_user.to_dict())
        output=users.find_one({'name':name,'email':email,'signum':user_signum})
        
        return json_util.dumps(output)
    if request.method=="GET":
       
        all_users=db.users.find({}) 
        list_users=[]
        for document in all_users:
            print(document)
            list_users.append(document)

        return json_util.dumps(list_users)

  
if __name__ =='__main__':  
    app.run(debug = False) 