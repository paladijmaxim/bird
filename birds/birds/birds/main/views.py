from django.shortcuts import render
from django.http import HttpResponse
from base.models import cards


def index(request):
    items = cards.objects.all() 
    context = {'items': items}
    return render(request, 'main/index.html',context)
