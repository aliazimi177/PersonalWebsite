from django.shortcuts import render,redirect
from django.views.generic import ListView
from .models import *
from .forms import *
# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = 'works.html'
    context_object_name = "posts"


def index(request):
    return render(request, "index.html")


class AboutMeView(ListView):
    template_name = 'about.html'
    model = Post


def contact(request):
    form = ContactForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('thanks')

    return render(request, "contact.html",  {'form': form})


def thanks(request):
    return render(request,'thank.html')