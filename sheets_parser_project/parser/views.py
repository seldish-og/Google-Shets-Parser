from pprint import pprint
from django.shortcuts import render
from django.http import HttpResponse
from .models import OrderModel
from google_api import google_sheets_parser
import time


def start_parser(request):
    all_entries = OrderModel.objects.all()
    print(all_entries)
    html = "<html><h1>SERVER IS RUNNING!!</h1></html>"
    return HttpResponse(html)
