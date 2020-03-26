import csv
import os


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
