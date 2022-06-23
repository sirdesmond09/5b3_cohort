from django.shortcuts import render
from django.http.response  import HttpResponse


def home(request):
    context = {
        "page": "home"
    }
    return render(request, "home.html", context)

def about(request):
    data = {
        "page": "about"
    }
    return render(request, "about.html", data)


def calculate_interest(request):
    s_i = None
    
    if request.method == "POST":
        principal = int(request.POST.get("principal"))
        rate = int(request.POST.get("rate"))
        time = int(request.POST.get("time"))
        
        s_i = round(principal*(rate/100)*time, 2)
        
    data = {
        "page": "calculator",
        "result" : s_i,
        
    }
    return render(request, "calculator.html", data)