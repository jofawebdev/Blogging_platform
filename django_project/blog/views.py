from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, PythonTutorial, DjangoGuide, DeveloperTool


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)



class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app_name>/<model_name>_list.html
    context_object_name = 'posts' # To match what is used in the function-based view
    ordering = ['-date_posted'] # order posts
    paginate_by = 5



class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' # <app_name>/<model_name>_list.html
    context_object_name = 'posts' # To match what is used in the function-based view
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')



class PostDetailView(DetailView):
    model = Post


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
    

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



# About page view
def about(request):
    context = {
        'title': 'About Us',
        'vision': 'To become the go-to educational platform for aspiring Python and Django developers.',
        'mission': 'Our mission is to provide high-quality, practical tutorials, tips, and resources to help developers at all levels master Python and Django development.',
        'core_values': [
            'Commitment to Quality',
            'Focus on Practical Skills',
            'Community and collaboration',
            'Continuous Learning',
        ],
        'objectives': [
            'To simplify python and Django concepts for developers of all levels.',
            'To foster a community of learners and developers who support each other.',
            'To provide up-to-date tutorials on the latest features in Python and Django.',
            'To promote best practices in coding and software development.'
        ]
    }
    return render(request, 'blog/about.html', context)



# View for Python Tutorials
def python_tutorials(request):
    tutorials = PythonTutorial.objects.all()
    context = {
        'title': 'Python Tutorials',
        'tutorials': tutorials
    }
    return render(request, 'blog/python_tutorials.html', context)



# View for Django Guides
def django_guides(request):
    guides = DjangoGuide.objects.all()
    context = {
        'title': 'Django Guides',
        'guides': guides
    }
    return render(request, 'blog/django_guides.html', context)



# View for Developer Tools
def developer_tools(request):
    tools = DeveloperTool.objects.all()
    context = {
        'title': 'Developer Tools',
        'tools': tools
    }
    return render(request, 'blog/developer_tools.html', context)