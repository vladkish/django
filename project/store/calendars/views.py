from django.shortcuts import render, HttpResponse
from datetime import datetime
import calendar
import locale
# Create your views here.

# requests -> вся информация о requests запросе.
def calendars(requests):
    x_forwarded_for = requests.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = requests.META.get('REMOTE_ADDR')
    return HttpResponse(ip)