from pprint import pprint
from django.shortcuts import render
from django.http import HttpResponse
from .models import OrderModel
from google_api import google_sheets_parser
import time


def add_data_db(data):
    for row in data:
        to_save = OrderModel(
            order_number=row[1],
            price_usd=int(row[2]),
            order_date=row[3],
            price_rub=float(row[4]),
        )
        to_save.save()


def start_parser(request):
    all_entries = OrderModel.objects.all()

    # sheets_data = google_sheets_parser.get_sheet_data()

    if not all_entries:
        # add_data_db(sheets_data)
        print("ss")
        # time.sleep(3600)
    else:
        # OrderModel.objects.all().delete()
        # add_data_db(sheets_data)
        print("ss")

        # time.sleep(3600)

    html = "<html><h1>PARSER STOPPED, CHECK ERRORS</h1></html>"
    return HttpResponse(html)
