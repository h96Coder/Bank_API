import json
from django.http import HttpResponse
import datetime


class BankCRUDMixin():
    def handle_request(self, *args, **kwargs):
        raise NotImplementedError

    def http_response(self, json_data, status=200):
        return HttpResponse(json_data, content_type="application/json", status=status)

    def get(self, request, *args, **Kwargs):
        """
        :param request:
        :param args:
        :param Kwargs:
        :return:
        """
        _json_data = self.parse_request(request)
        data = self.handle_request(_json_data)
        return self.http_response(json.dumps(data))

    def parse_request(self, request):
        data = request.body
        valid_json = self.valid_json(data)
        if not valid_json:
            return self.http_response(json.dumps({"msg": "invalid format"}), status=404)
        json_data = json.loads(data)

        return dict, json_data

    def valid_json(self, data):
        try:
            data = json.loads(data)
            valid_json = True
        except:
            valid_json = False

        return valid_json

    def bank_date(self, day, month):
        try:
            month = datetime.datetime.strptime(month, "%b").month
        except:
            month = datetime.datetime.strptime(month, "%B").month

        date = datetime.date(year=datetime.datetime.today().year, day=int(day), month=month)
        return date

# class HttpResponseMixin():
