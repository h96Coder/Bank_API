import csv
import os
class readcsvsingleton:
   __instance = None
   @staticmethod
   def getInstance():
      if readcsvsingleton.__instance == None:
         readcsvsingleton()
      return readcsvsingleton.__instance
   def readcsvfile(self):
      loc=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"csvfile/bank.csv")
      with open(loc, mode='r') as csv_file:
          csv_reader = csv.DictReader(csv_file, delimiter=";",)
          listdict=[]
          for reader in csv_reader:
              listdict.append(reader)
          return  listdict
   def __init__(self):
      if readcsvsingleton.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         self.csv_reader=self.readcsvfile()
         readcsvsingleton.__instance = self
s = readcsvsingleton.getInstance()

