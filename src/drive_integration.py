import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import HttpError, build

spreadsheet_id = '1lFRh-nVBFLvlYA-LjF9p-3V3SVrL-IKlsa_4mxKuE18'


def setup_credentials():
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return creds


def access_spreadsheet(creds):
    try:
        service = build("sheets", "v4", credentials=creds)
        sheet = service.spreadsheets()
        return sheet
    except HttpError as err:
        print(err)

def format_data(data):
    values = []
    for item in data['items']:
        values.append([item['date'], item['name'], item['value']])
    return values

def append_data(sheet, values):
    try:

        body = {"values": values}
        result = (
            sheet.values()
            .append(
                spreadsheetId=spreadsheet_id, 
                range="A1:C1",
                valueInputOption= "USER_ENTERED",
                body=body,
            )
            .execute()
        )
        print(f"{(result.get('updates').get('updatedCells'))} cells appended.")
    except HttpError as err:
        print(err)
        
        
def import_data(data):
    creds = setup_credentials()
    sheet = access_spreadsheet(creds)
    values = format_data(data)
    append_data(sheet, values)
