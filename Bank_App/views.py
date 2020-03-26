from django.views.generic import View
from Bank_App.mixins import BankCRUDMixin,HttpResponseMixin
import json

class BankContact(BankCRUDMixin,HttpResponseMixin,View):
    def get(self,request,*args,**Kwargs):
        data=request.body
        valid_json=self.valid_json(data)
        if not valid_json:
            return self.http_response(json.dumps({"msg":"invalid format"}),status=404)
        json_data=json.loads(data)
        dict=self.dictlist()
        dcellular=[]
        for d in dict:
            if d.get("contact") != json_data.get("contact"):
                dcellular.append(d)
        return self.http_response(json.dumps(dcellular))


class BankDayMonthFilter(HttpResponseMixin,BankCRUDMixin,View):
    def get(self,request,*args,**Kwargs):
        data=request.body
        valid_json=self.valid_json(data)
        if not valid_json:
            return self.http_response(json.dumps({"msg":"invalid format"}),status=404)
        json_data=json.loads(data)
        dict=self.dictlist()
        ddate=[]
        for d in dict:
            if self.bank_date(d.get("day"),d.get("month")) >= self.bank_date(json_data.get("day"),json_data.get("month")):
                ddate.append(d)
        return self.http_response(json.dumps(ddate))


class BankMarital(HttpResponseMixin,BankCRUDMixin,View):
    def get(self,request,*args,**Kwargs):
        data=request.body
        valid_json=self.valid_json(data)
        if not valid_json:
            return self.http_response(json.dumps({"msg":"invalid format"}),status=404)
        json_data=json.loads(data)
        dict=self.dictlist()
        dmarital=[]
        for d in dict:
            if json_data.get("start_age")< int(d.get("age"))and json_data.get("end_age")>int(d.get("age")) and json_data.get("marital_status")==d.get("marital"):
                dmarital.append(d)
        return self.http_response(json.dumps(dmarital))

