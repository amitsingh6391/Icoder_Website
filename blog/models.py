from django.db import models



class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content =models.CharField(max_length=3050)
    author = models.CharField(max_length=50)

    slug = models.CharField(max_length=150)
   
    timeStamp = models.DateTimeField(blank=True)


    def __str__(self):
        return  self.title  + " By - " + self.author
