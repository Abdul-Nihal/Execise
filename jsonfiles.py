import json
with open('data.json') as json_file:
    data = json.load(json_file)
    print("Type:", type(data))
#print(data)
#json into dictnory
dict={}
for i in data:
    dict[i["id"]]=[i["first_name"],i["dept"]]
print(dict)
#print names of all student
for i in data:
    print(i['first_name'])
#create json file by categirizing dept
dict1={}
for i in data:
    if i["dept"]=="EC":
        a=i["first_name"]
        dict1.setdefault('EC', []).append(a)
    elif i["dept"]=="IT":
        a=i["first_name"]
        dict1.setdefault('IT', []).append(a)
print(dict1)
with open("data_dept.json", "w") as outfile:
    json.dump(dict1, outfile)
#reading city
for i in data:
    print(i["address"]["city"])
#id of students in merit list
for i in data:
    if i["merit"]==True:
        print(i["id"])
