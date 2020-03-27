from django.views.generic import View
from Bank_App.mixins import BankCRUDMixin
from Bank_App import readcsvsingleton
csv_file = readcsvsingleton.readcsvsingleton().csv_reader
sheet_file = readcsvsingleton.readcsvsingleton().sheetreader

class BankContact(BankCRUDMixin, View):

    def handle_request(self, _json_data):
        _dict=self.sheetorcsv(_json_data,csv_file,sheet_file)
        return [d for d in _dict if d.get("contact") != _json_data.get("contact")]


class BankDayMonthFilter(BankCRUDMixin, View):

    def handle_request(self, _json_data):
        _dict = self.sheetorcsv(_json_data, csv_file, sheet_file)
        return [d for d in _dict if
                self.bank_date(d.get("day"), d.get("month")) >= self.bank_date(_json_data.get("day"),
                                                                               _json_data.get("month"))]


class BankMarital(BankCRUDMixin, View):
    _dict = csv_file

    def handle_request(self, _json_data):
        _dict = self.sheetorcsv(_json_data, csv_file, sheet_file)
        return [d for d in _dict if _json_data.get("start_age") < int(d.get("age")) and _json_data.get("end_age") > int(d.get("age")) and _json_data.get("marital_status") == d.get("marital")]
