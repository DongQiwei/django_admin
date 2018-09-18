from django.shortcuts import render

from hm.models import Img


def index(request):
    imgs = Img.objects.all()
    return render(request, 'index01.html', locals())
