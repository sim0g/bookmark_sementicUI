from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Bookmark

# Create your views here.
class BookmarkList(ListView):
    model = Bookmark
    paginate_by = 3 # 한 페이지에 최대 몇개 나올지 쓰는거

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'
    success_url = reverse_lazy('list')

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    # field = ['site_name', 'url']
    success_url = reverse_lazy('list')

