from django.http import HttpResponse
from django.shortcuts import render,render_to_response
from django.template.response import TemplateResponse
# Create your views here.

def test_middle(request):
    tr = TemplateResponse(request, 'index.html')
    try:
        print('test_middle')
        int('adc')
    except:
        pass
    return tr.render()
