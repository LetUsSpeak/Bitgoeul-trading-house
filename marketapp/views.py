from django.shortcuts import render

# Create your views here.

def landing(request):
    return render(
        request,
        'marketapp/landing.html'
    )

def metaverse(request):
    return render(
        request,
        'marketapp/metaverse.html'
    )