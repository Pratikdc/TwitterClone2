from urllib import request
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from posts.forms import Postform
from .models import Post

# Create your views here.


def index(request):
    # If the method is POST
    if request.method == 'POST':
        form = Postform(request.POST)
        # If the form is valid
        if form.is_valid():
            # yes save
            form.save()

            # redirect to home
            return HttpResponseRedirect('/')
        else:
            # no show error
            return HttpResponseRedirect(form.errors.as_json)

    posts = Post.objects.all()[:20]

    return render(request, 'posts.html',
                  {'posts': posts})


def delete(request, post_id):
    # Find post
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')
