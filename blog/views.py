from django.shortcuts import render, get_object_or_404
from .models import Post 
from .forms import FeedBackForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def home(request):
    form = FeedBackForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    return render(request, 'blog/home.html', {'form': form})


def article_detail(request, slug):
    form = FeedBackForm(request.POST or None)
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/' + slug)

    return render(request, 'blog/page.html', {
        'post': post,
        'form': form
        })
