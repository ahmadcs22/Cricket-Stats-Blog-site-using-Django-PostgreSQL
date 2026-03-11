from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

def index(request):
    # return HttpResponse("this is homepage")
    return render(request,"index.html",)
def about(request):
    return render(request,"about.html")
def stats(request):
    return render(request,"stats.html")
def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        contact=Contact(name=name,email=email,subject=subject,message=message,date=datetime.today())
        contact.save()
        messages.success(request,"submitted successfully !")
    return render(request,"contact.html")

