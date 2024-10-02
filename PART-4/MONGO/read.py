import pymongo

Client=pymongo.MongoClient('mongodb://localhost:27017/')
    
    
db = Client['11AM']
user_col = db['user']
user_list = user_col.find()

print(type(user_col))
print(type(user_list))

for user in user_list:
    print(user[id])

Client.close()
