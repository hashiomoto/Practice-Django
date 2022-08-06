from django.shortcuts import render
from .models import Post # Postモデルをimport
from django.urls import reverse_lazy
from .forms import PostCreateForm # forms.py で作ったクラスをimport
# Create your views here.

from django.views import generic

class PostListView(generic.ListView): # generic の ListViewクラスを継承
    model = Post # 一覧表示させたいモデルを呼び出し

class PostCreateView(generic.CreateView): # 追加
    model = Post # 作成したい model を指定
    form_class = PostCreateForm # 作成した form クラスを指定
    success_url = reverse_lazy('blog:post_list') # 記事作成に成功した時のリダイレクト先を指定
    
class PostDetailView(generic.DetailView): # 追加
    model = Post  # pk(primary key)はurls.pyで指定しているのでここではmodelを呼び出すだけで済む
    
class PostUpdateView(generic.UpdateView): # 追加
    model = Post
    form_class = PostCreateForm # PostCreateFormをほぼそのまま活用できる
    success_url = reverse_lazy('blog:post_list')
class PostDeleteView(generic.DeleteView): # 追加
    model = Post
    success_url = reverse_lazy('blog:post_list')