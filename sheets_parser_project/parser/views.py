from django.shortcuts import render
from django.http import HttpResponse
from google_sheets import google_sheets_api


def start_parser(request):
    data = google_sheets_api.get_sheet_data()
    return HttpResponse(data)
