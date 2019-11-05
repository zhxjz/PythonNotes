import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["shuoshuo"]
mycol = mydb["text"]

for x in mycol.find():
    print(x)
