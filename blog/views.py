from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    # Query for posts published in the past, ordered by published date
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # Pass the QuerySet to the template
    return render(request, 'blog/post_list.html', {'posts': posts})