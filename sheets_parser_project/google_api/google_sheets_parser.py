from pprint import pprint
import os
from re import U
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
from .currency_change import cbr_api

basedir = os.path.abspath(os.path.dirname(__file__))
CREDENTIALS_FILE = basedir+'/creds.json'


def add_rub_value(values):
    usd_price = cbr_api.get_usd_price()
    for row in values:
        converted_usd_to_rub = (int(row[2]) * float(usd_price))
        row.append(converted_usd_to_rub)
    return values


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

    # Чтение файла
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A:E',
        majorDimension='ROWS'
    ).execute()["values"][1:]

    updated_values = add_rub_value(values=values)

    return updated_values
