import os
import csv
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import gspread

class googlesheet:

    def cred(self):
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
                 "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "csvfile/creds.json"), scope)
        return creds

    def writegooglesheet(self,reader_values):
        creds=self.cred()
        service = build('sheets', 'v4', credentials=creds)
        spreadsheet = {
            'properties': {
                'title': 'Bank'
            }
        }
        spreadsheet = service.spreadsheets().create(body=spreadsheet,fields='spreadsheetId').execute()
        spreadsheetid=spreadsheet.get('spreadsheetId')
        Response_date = service.spreadsheets().values().update(
                spreadsheetId=spreadsheetid,
                valueInputOption='RAW',
                range='A1:'+'Z'+str(len(reader_values)),
                body=dict(
                    majorDimension='ROWS',
                    values=reader_values)).execute()

    def readgooglesheet(self):
        creds=self.cred()
        client=gspread.authorize(creds)
        sheet= client.open("Bank").sheet1
        #print(sheet.get_all_records())
        return (sheet.get_all_records())
