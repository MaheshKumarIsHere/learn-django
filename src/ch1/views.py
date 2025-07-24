from django.shortcuts import render



# Create your views here.
def home(request):
    return render(request,"ch1/home.html")


def map(request):
    return render(request,"ch1/map.html")