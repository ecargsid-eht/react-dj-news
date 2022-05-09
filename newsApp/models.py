from django.db import models

# Create your models here.


class Category(models.Model):
    cat_title = models.CharField(max_length=200)

    def __str__(self):
        return self.cat_title
    

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    content = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title