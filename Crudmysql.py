from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Abdul@123'
app.config['MYSQL_DB'] = 'sakila'
mysql = MySQL(app)

@app.route('/')
def a():
    return 'a'
@app.route('/employee', methods =['GET'])
def employee():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM employee1')
    account = cursor.fetchone()
    rows = cursor.fetchall()
    print(rows)
    return jsonify(rows)
@app.route('/employee/new', methods =['POST'])
def empnew():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    empid1=request.form['empid']
    fname1= request.form['fname']
    lname1= request.form['lname']
    deptid1 = request.form['deptid']
    cursor.execute('INSERT INTO employee1 VALUES ( % s, % s, % s, % s)',(empid1,fname1,lname1,deptid1))
    mysql.connection.commit()
    return "successfully added new employee"
@app.route('/employee/update', methods =['POST','PUT'])
def empupdate():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    empid1=request.form['empid']
    fname1= request.form['fname']
    lname1= request.form['lname']
    deptid1 = request.form['deptid']
    cursor.execute('UPDATE employee1 SET fname=%s, lname=%s, deptid=%s WHERE empid=%s',(fname1,lname1,deptid1,empid1,))
    mysql.connection.commit()
    return "successfully updated employee"

@app.route('/employee/delete/<int:id>', methods=['DELETE'])
def delete_user(id):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("DELETE FROM employee1 WHERE empid=%s", (id,))
    mysql.connection.commit()
    return "successfully deleted employee"
if __name__ == "__main__":
    app.run(host ="localhost", port = int("5000"))
