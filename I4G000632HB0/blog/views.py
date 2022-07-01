from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Post
from django.urls import reverse_lazy

class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("blog:all")

class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"

class PostDetailView(DetailView):
    model = Post
    fields = "__all__"
    template_name = "blog/post_detail.html"
    success_url = reverse_lazy("blog:all")

class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("blog:all")

class PostDeleteView(DeleteView):
    model = Post
    fields = "__all__"
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("blog:all")
