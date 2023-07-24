from flask import Flask, render_template
import os
import pymongo

URL = 'mongodb+srv://admin:root@atlascluster.tp46zhe.mongodb.net/'
client = pymongo.MongoClient(URL)

db = client['Students']

students = [
    {'name':'David','country':'UK','city':'London','age':34},
    {'name':'John','country':'Sweden','city':'Stockholm','age':28},
    {'name':'Sami','country':'Finland','city':'Helsinki','age':25}
]

for student in students:
    db.students.insert_one(student)

app = Flask(__name__)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)