from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

#lets import the posts .models just means lets use models in this directory
from .models import Post


posts = [
    {
        'author': 'Dennis',
        'title' : 'This is the Title',
        'content': 'This is the content for the blog post',
        'date_posted': 'March, 8th, 2021'
    },
    {
        'author': 'Jane',
        'title' : 'This is the Title 2',
        'content': 'This is the content for the blog post 2',
        'date_posted': 'March, 7th, 2021'
    }
]


def home(request):
    #creating a dictionary for the content of the post
    context = {
        'posts': Post.objects.all() #takes all the posts in the database
    }
    #passing the context to the template will allow us to access it in template
    return render(request, 'blog/home.html', context)

#for using the same blog using the ListView
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

#create the detail view for the page
class PostDetailView(DetailView):
    model = Post

#create the create view for the blog post will be a form
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # Test function to check if post was done by user before updaating
    def test_func(self):
        # get the current post
        post = self.get_object()
        # check if current user matches post
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog/'

    # run the same test to check if existing user is deleting.
    def test_func(self):
        # get the current post
        post = self.get_object()
        # check if current user matches post
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})