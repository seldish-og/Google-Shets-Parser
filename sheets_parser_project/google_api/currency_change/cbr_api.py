from cgitb import text
from datetime import date, datetime, timedelta
import requests
from lxml.etree import fromstring


URL = "https://www.cbr.ru/scripts/XML_dynamic.asp"


def create_date(flag=False):
    if flag:
        date_ = datetime.now() - timedelta(days=1)
    else:
        date_ = date.today()
    formated_date = date_.strftime("%d/%m/%Y")
    print(formated_date)
    return formated_date


def send_request_api(date=create_date()):
    params = {
        "date_req1": date,
        "date_req2": date,
        "VAL_NM_RQ": "R01235"
    }

    responce = requests.get(url=URL, params=params)
    return responce


def read_xml(responce):
    responce_xml = fromstring(responce.content)
    usd_price = responce_xml.xpath('/ValCurs/Record/Value').pop()
    usd_price_formated = usd_price.text.replace(",", ".")

    return usd_price_formated


def get_usd_price():
    responce = send_request_api()
    try:
        usd_price_formated = read_xml(responce)

    except IndexError as index_error:
        responce = send_request_api(date=create_date(True))
        usd_price_formated = read_xml(responce)
    return float(usd_price_formated)
