import csv
import os
import json
from Bank_App.googlesheet import googlesheet
class readcsvsingleton:
    __instance = None

    def __new__(cls, *args):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args)
            cls.__instance.init(*args)
        return cls.__instance

    def init(self, *args, **kwargs):
        loc = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "csvfile/bank.csv")
        with open(loc, mode='r') as csv_file:
            self.csv_reader = [reader for reader in csv.DictReader(csv_file, delimiter=";", )]
            read_csv2 = csv.DictReader(open(loc, mode='r'), delimiter=";", )
            fieldname = read_csv2.fieldnames
            reader_values = [list(reader.values()) for reader in read_csv2]
            reader_values.insert(0, fieldname)
            googlesheet().writegooglesheet(reader_values)
            self.sheetreader =googlesheet().readgooglesheet()
            #print(self.sheetreader)


