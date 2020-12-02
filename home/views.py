

# Create your views here.
from django.shortcuts import render,HttpResponse



# Create your views here.

def home(request):
    return render(request,'home/home.html',)
    # return HttpResponse("this is home")
def about(request):
    return render(request,'home/about.html',)
    #return HttpResponse("this is about")
def contact(request):
    #return HttpResponse("this is contact")
     return render(request,'home/contact.html',)