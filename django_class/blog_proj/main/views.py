from django.shortcuts import render, get_object_or_404
from .models import Post




def post_list(request):
    object_list = Post.objects.filter(status="published")
    
    data = {
        
        "posts" : object_list,
        
    }
    
    return render(request,'blog/post/list.html', data)
    
    
    
def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, status='published',
                             publish__year=year, 
                             publish__month=month, 
                             publish__day=day, 
                             slug=slug)
    
    
    data = {
        
        "post" : post,
        
    }
    
    return render(request,'blog/post/detail.html', data)
    