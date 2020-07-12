from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import postgresql_api
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

@app.route('/')
def root():
    return "เปิดได้แล้ววว YeHaa ไปหน้า <a href='/home?name=safe'>home</a>"

@app.route('/home')
def home():
    username = request.args.get('name')
    print(username,'<-----------')
    return username + " มาหน้า home แล้ว ไปหน้า  commit อิกรอบละกันน<a href='/'>แรก</a>"

@app.route('/sum')
def mySum():
    a = request.args.get('a')
    b = request.args.get('b')
    a = int(a)
    b = int(b)
    return  str(a+b)

@app.route('/mypage')
def mypage():
    name = request.args.get('name')
    return render_template('home.html',name=name)

@app.route('/studentlist')
def studentList():
    studentList = postgresql_api.getStudentData()
    return render_template('StudentList.html',studentList=studentList)
if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0", port=5000)