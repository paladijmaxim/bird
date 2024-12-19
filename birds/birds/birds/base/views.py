from django.shortcuts import render

def base_birds(request):
    return render(request, 'main/index.html')