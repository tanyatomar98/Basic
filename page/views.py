from django.shortcuts import render
from django.http import HttpResponse, request
# Create your views here.
def home_page_view(request ,*args, **kwargs):
    print(args, kwargs)
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})

def blog_view(request, *args, **kwargs):
    myCon = {
        "my_text": "This is my text from dictionary",
        "my_number": 907,
        "my_list": ["tanya", "Neelanshu", "baby"]
    }
    return render(request, "blog.html", myCon)