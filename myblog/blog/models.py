from django.db import models
from django.utils.html import format_html
# Create your models here.

#Category Model 

class Category(models.Model):
    cat_td = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/')
    add_date = models.DateField(auto_now_add=True, null=True)

    def image_tag(self):
        return format_html('<img src="/media/{}" style="width:60px; height:60px;" />'.format(self.image))


# Blog Post Model 
class Post(models.Model):
    post_td = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    url = models.CharField(max_length=100)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/')

