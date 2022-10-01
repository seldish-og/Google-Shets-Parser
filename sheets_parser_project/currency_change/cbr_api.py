from datetime import date
import requests
from lxml.etree import fromstring


URL = "https://www.cbr.ru/scripts/XML_dynamic.asp"


def today():
    today = date.today()

    formated_today = today.strftime("%d/%m/%Y")
    return formated_today


def convert_usd_to_rub(rub_amount):
    now_date = today()
    params = {
        "date_req1": now_date,
        "date_req2": now_date,
        "VAL_NM_RQ": "R01235"
    }

    responce = requests.get(url=URL, params=params)
    xml_responce = fromstring(responce.content)
    test = xml_responce.xpath('/ValCurs/Record/Value').pop()
    return test.text


print(convert_usd_to_rub(10))
