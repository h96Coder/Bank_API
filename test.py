import requests
import json
Base_Url="http://127.0.0.1:8000/"

def getcontact(contact):
    endpoint = 'BankContact/'
    data={
        'contact':contact
    }
    data=json.dumps(data)
    response=requests.get(Base_Url+endpoint,data=data)
    print(json.dumps(response.json(),indent=4))

def getdates(day,month):
    endpoint = 'BankDayMonthFilter/'
    data={
        'day':day,
        'month':month
    }
    data=json.dumps(data)
    response=requests.get(Base_Url+endpoint,data=data)
    print(json.dumps(response.json(),indent=4))

def getMarital(start_age,end_age,marital_status):
    endpoint = 'BankMarital/'
    data={
        'start_age':start_age,
        'end_age':end_age,
        'marital_status':marital_status
    }
    data=json.dumps(data)
    response=requests.get(Base_Url+endpoint,data=data)
    print(json.dumps(response.json(),indent=4))
getMarital(20,50,"married")