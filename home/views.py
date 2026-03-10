from django.shortcuts import render,HttpResponse

def index(request):
    # return HttpResponse("this is homepage")
    return render(request,"index.html",)
def about(request):
    return render(request,"about.html")
def stats(request):
    return render(request,"stats.html")
def contact(request):
    return render(request,"contact.html")

