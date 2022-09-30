from pprint import pprint
import os
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials


basedir = os.path.abspath(os.path.dirname(__file__))
CREDENTIALS_FILE = basedir+'/creds.json'


def get_sheet_data():

    # ID Google Sheets документа (можно взять из его URL)
    spreadsheet_id = '18ZoL_HVZcJj_jNQgi3sMKeiCPEnSMXM0JSIKbcpCuJ4'

    # Авторизуемся и получаем service — экземпляр доступа к API
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE,
        ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)

    # Пример чтения файла
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A:E',
        majorDimension='ROWS'
    ).execute()
    pprint(values)
    return values


get_sheet_data()
