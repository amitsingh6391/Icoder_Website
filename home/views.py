

# Create your views here.
from django.shortcuts import render,HttpResponse

from django.contrib import messages
from home.models import Contact
from blog.models import Post


# Create your views here.

def home(request):
    return render(request,'home/home.html',)
    # return HttpResponse("this is home")
def about(request):
    return render(request,'home/about.html',)
    #return HttpResponse("this is about")
def contact(request):
    #return HttpResponse("this is contact")
   

    if request.method=="POST":

        
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']

        print(name,email,phone,content)

        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
             messages.error(request, 'Please fill the formcorrectly.')

        else:

         
        
          contact = Contact(name=name,email=email,phone=phone,content=content)
          contact.save()
          messages.success(request, 'Your meesage has been send.')



      

      
    

    return render(request,'home/contact.html',)

def search(request):

     query = request.GET['query']

     if len(query)>78:
         allPosts= Post.objects.none()
     else:
         allPostsTitle =Post.objects.filter(title__icontains=query)
        
         allPostContentent = Post.objects.filter(content__icontains = query)
         
         allPosts = allPostsTitle.union(allPostContentent)
     
     if allPosts.count() ==0:
          messages.warning(request, 'no search result found Please reweite your query.')  
     params = {"allPosts":allPosts,"query":query}
 
     return render(request,'home/search.html',params)

    
    # return HttpResponse("This is you serach")