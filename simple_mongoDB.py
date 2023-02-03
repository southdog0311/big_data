from unicodedata import name
from pymongo import MongoClient
import pprint

client = MongoClient("mongodb+srv://1092929:sam031191@1092929.6dhzsux.mongodb.net/?retryWrites=true&w=majority")
db = client['test']
collection = db['Classes']

students = [
    {
        'class_id': 'c2',
        'class_name': 'Home fusion made easy'
    },
    {
        'class_id': 'c3',
        'class_name': 'How to train an attack iguana'
    },
    {
        'class_id': 'c4',
        'class_name': 'Learn SQL for fun and profit'
    }
]

# result = collection.insert_many(students) //prevent repetition insert
# print(result.inserted_ids)    //prevent print

first = collection.find()
for record in first:
    print(record)
print("--------------------")
collection = db['Students']

name = [
    
    {
        'student_id': 's2',
        'student_name': 'Rick'
    },
    {
        'student_id': 's3',
        'student_name': 'Susanna'
    },
    {
        'student_id': 's4',
        'student_name': 'Jennifer'
    }
]

# result = collection.insert_many(name) //prevent repetition insert
# print(result.inserted_ids)    //prevent print

second = collection.find()
for record in second:
    print(record)
print("--------------------")
collection = db['Grades']

score = [
    
    {
        'student_id': 's2',
        'class_id': 'c1',
        'grade': 99
    },
    {
        'student_id': 's3',
        'class_id': 'c1',
        'grade': 65
    },
    {
        'student_id': 's4',
        'class_id': 'c1',
        'grade': 3
    },
    {
        'student_id': 's2',
        'class_id': 'c2',
        'grade': 38
    },
    {
        'student_id': 's3',
        'class_id': 'c2',
        'grade': 88
    },
    {
        'student_id': 's4',
        'class_id': 'c2',
        'grade': 48
    },
    {
        'student_id': 's1',
        'class_id': 'c3',
        'grade': 7
    },
    {
        'student_id': 's4',
        'class_id': 'c3',
        'grade': 32
    },
    {
        'student_id': 's1',
        'class_id': 'c4',
        'grade': 94
    },
    {
        'student_id': 's2',
        'class_id': 'c4',
        'grade': 63
    },
    {
        'student_id': 's3',
        'class_id': 'c4',
        'grade': 75
    },
    {
        'student_id': 's4',
        'class_id': 'c4',
        'grade': 20
    }
]

# result = collection.insert_many(score)    //prevent repetition insert
# print(result.inserted_ids)    //prevent print

third = collection.find()
for record in third:
    print(record)
print("--------------------")

result=db.Grades.find({"class_id": 'c2'})
for i in result:
    student_id = i["student_id"]
    j=db['Students'].find({"student_id":student_id})[0]["student_name"]
    print(j)


print("--------------------")
for k in db.Grades.find({"class_id": 'c4', "student_id":'s4'}):
    print(k["grade"])
