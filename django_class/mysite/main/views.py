from django.shortcuts import render
from django.http.response  import HttpResponse


def home(request):
    
    return HttpResponse("<h3>Welcome to cohort 5b3!</h3>")

def about(request):
    
    return HttpResponse("<h3>This is what is about us!</h3>")


def calculate_interest(request, principal, rate, time):
    s_i = principal*(rate/100)*time
    
    return HttpResponse(f"""<h2 style="color:red">Simple Interest</h2>
    <p>The simple interest is {s_i}</p>""")