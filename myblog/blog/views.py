from django.shortcuts import render
from django.http import HttpResponse
from blog .models import Post

# Create your views here.
def home(request):
    post_data = Post.objects.all()[:10]
    print("***post_data******",post_data)
    data = {
        'post':post_data
    }
    return render(request,'home.html', data)


def post(request,url):
    post = Post.objects.get(url=url)
   
    return render(request,'post.html', {'post':post})