from django.shortcuts import render,HttpResponse



# Create your views here.
def blogHome(request):
    return render(request,"blog/blogHome.html")
    #return HttpResponse("this is blog home we will keep all post here")


def blogPost(request,slug):
     return render(request,"blog/blogPost.html")
  #  return HttpResponse(f"this is blogpost:{slug}")