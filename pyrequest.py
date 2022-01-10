import requests # request mean you send the request 
import json


headers = {'content-Type':'application/json'}
def getdata(id=None):
    URL = "http://127.0.0.1:8000/empenfo/27"
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url=URL,headers=headers,data=json_data) # request.get mean you send the request to this api or this website to visit 
    data = r.json()
    print(data)
getdata()


 # request.get mean you send the request to this api or this website to visit 
def dataenter():
    # use to put mean enter the  
    URL1 = "http://127.0.0.1:8000/empenfo/" 
    data1 = {
    "first_name": "sudhir",
    "last_name": "Ruta",
    "company_name": "Buckley Miller & Wright",
    "city": "Chagrin Falls",
    "state": "OH",
    "zip": 44023,
    "email": "gsuta@cox.net",
    "web": "http://www.buckleymillerwright.com",
    "age": 44
    }
    json_data = json.dumps(data1)
    r = requests.post(url=URL1,headers=headers,data=json_data)
    d = r.json()
    print(d)
#dataenter()


def updatedata():
  # use to update the data of table 
   # enter the number of id in link to update the by id number
   # for example URL2 = "http://127.0.0.1:8000/empenfo/1"
    URL2 = "http://127.0.0.1:8000/empenfo/"
    data_up = {
    "id": 12,
    "first_name": "Shahid",
    "last_name": "kapoor",
    "age":29
    }
    json_data = json.dumps(data_up)
    r = requests.put(url=URL2,headers=headers,data=json_data)
    d = r.json()
    print(d)
#updatedata()

def deletedata():
   # use to delete the data of table  
   # just give id num example URL1 = "http://127.0.0.1:8000/empenfo/2"
    URL2 = "http://127.0.0.1:8000/empenfo/"
    r = requests.delete(url=URL2,headers=headers)
    d = r.json()
    print(d)
    
#deletedata()    

'''
rd = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
print(rd.text) # rd text mean the text in webstie or code will show you
print(rd.status_code) # rd.status code mean status of your code that you can search in internet
#print(r.text)
# note there are many type of request now we learn about get but after some time we will learn about post request
'''