import pymongo

Client=pymongo.MongoClient('mongodb://localhost:27017/')
    
    
db = Client['11AM']
user_col = db['USER']
user_list = user_col.find()



for user in user_list:
    print(user)

Client.close()

 