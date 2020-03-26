'''
Part 1: Store the data in Google Spreadsheet.
Part 2: Create a webservice using  Django which can handle below requests
from the client side, using Google Sheets as the source. The request and response must be in JSON format.
 '''

import requests
import json
Base_Url="http://127.0.0.1:8000/"

'''1. Show how many records that do not have "cellular" contact.'''

def getcontact(contact):
    endpoint = 'BankContact/'
    data={
        'contact':contact
    }
    data=json.dumps(data)
    response=requests.get(Base_Url+endpoint,data=data)
    print(json.dumps(response.json(),indent=4))
#getcontact("cellular")

'''2. Use "day" and "month" column values and find records which are after 15th October'''

def getdates(day,month):
    endpoint = 'BankDayMonthFilter/'
    data={
        'day':day,
        'month':month
    }
    data=json.dumps(data)
    response=requests.get(Base_Url+endpoint,data=data)
    print(json.dumps(response.json(),indent=4))

#getdates(15,"oct")

'''3. How many records having a specific marital status and between certain age group.'''

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

#getMarital(20,50,"married")