import requests
#get using main server
response = requests.get("http://127.0.0.1:5000/")
print(response.text)
#get with query using request2.py server
query = {'id':'1'}
response1 = requests.get('http://127.0.0.1:5000/api/v1/resources/books', params=query)
print("get with query",response1.text)

#post using sql server
requests.post('http://127.0.0.1:5000/employee/new', data={'empid':'9029','fname':'ABDULNIHAL','lname':'neelu','deptid':'103'})
#update using sql server
requests.put('http://127.0.0.1:5000/employee/new', data={'empid':'9029','fname':'ABDULNIHAL123','lname':'neelu123','deptid':'103'})

#some confusions with delete operation