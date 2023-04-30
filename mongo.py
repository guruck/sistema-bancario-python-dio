'''classe para testar mongoDB com python'''
from datetime import datetime
import pprint as pp
import pymongo as pyM

client = pyM.MongoClient('mongodb://localhost:27017/?readPreference=\
                         primary&appname=MongoDB%20Compass&ssl=false')

db = client.test

print(f'db.list_database_names: {client.list_database_names()}\n')
print(f'test.list_collection_names: {db.list_collection_names()}\n')

post = {
    'autor': 'Tiago1',
    'text': 'meu primeiro mongodb app baseado em python',
    'tags': ['mongodb', 'python', 'pymongo'],
    'date': datetime.utcnow()
}

posts = db.posts
# post_id = posts.insert_one(post).inserted_id
POST_ID = '64487950778a3bace0ca825c'
print(f'post_id: {POST_ID}\n')
pp.pprint(posts.find_one())

bulk_post = [{
    'autor': 'Tiago2',
    'text': 'meu segundo mongodb app baseado em python',
    'tags': ['mongodb', 'python', 'pymongo'],
    'date': datetime.utcnow()
    },
    {
    'autor': 'Tiago3',
    'text': 'esse trem aqui é parrudo!!',
    'title': 'Mongo is powerfull database',
    'tags': ['mongodb', 'python', 'pymongo'],
    'date': datetime.utcnow()
}]
# result = posts.insert_many(bulk_post)
RESULT = "[ObjectId('64487dc9d227208165676a65'), \
    ObjectId('64487dc9d227208165676a66')]"
print(f'results: {RESULT}')
print('\nall_posts:\n')
# for post in posts.find({"autor":"Tiago"}):
for post in posts.find():
    pp.pprint(post)

print(posts.count_documents({'tags': 'python'}))
# result = db.profiles.create_index([('author', pyM.ASCENDING)], unique=True)
print(sorted(list(db.profiles.index_information())))

# user_profile = [{'user_id':211,'author':'Tiago1'},\
# {'user_id':212,'author':'Tiago2'},{'user_id':213,'author':'Tiago3'}]
# result = db.profiles.insert_many(user_profile)

# db['profiles'].drop()
# posts.delete_one({'_id':'64487dc9d227208165676a65'})
