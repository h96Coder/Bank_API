from Bank_App import readcsvsingleton
import json
from django.http import HttpResponse
import datetime

class BankCRUDMixin():
    def dictlist(self):
        try:
            s = readcsvsingleton.readcsvsingleton()
            s.readcsvfile()
            dict = s.csv_reader
        except:
            s = readcsvsingleton.readcsvsingleton.getInstance()
            dict = s.csv_reader
        return dict
    def valid_json(self, data):
        try:
            data = json.loads(data)
            valid_json = True
        except:
            valid_json = False
        return valid_json
    def bank_date(self,day,month):
        try:
          month=datetime.datetime.strptime(month,"%b").month
        except:
            month = datetime.datetime.strptime(month, "%B").month
        date=datetime.date(year=datetime.datetime.today().year,day=int(day), month=month)
        return date
class HttpResponseMixin():
    def http_response(self,json_data,status=200):
        return HttpResponse(json_data,content_type="application/json",status=status)
