""" Playground views. """

# Django
from django.http import HttpResponse

# utilities
from datetime import datetime
import json


def hello_world(request):
    """ Greeting. """
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f'Hello World! current datetime is {now}')

def hi(request):
    """Hi."""
    res = {
        'data': request.GET['numbers'],
    }
    return HttpResponse(
        json.dumps(res, indent=2),
        content_type='application/json'
    )