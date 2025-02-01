from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm
from .models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def home(request):
    post = Post.objects.all().order_by('-date_posted')
    return render(request, 'blog/home.html', {'posts': post})


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})


def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post(
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content'],
                author=form.cleaned_data['author']
            )
            post.save()
            return redirect('blog-home')  # Redirect to home page after saving
    else:
        form = PostForm()

    return render(request, 'blog/create_post.html', {'form': form})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog-home')
    else:
        form = RegisterForm()
    return render(request, "blog/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('blog-home')
    return render(request, "blog/login.html")


def logout_view(request):
    logout(request)
    return redirect("blog-home")