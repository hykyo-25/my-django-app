from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .models import Video

class VideoList(generic.ListView):
    model = Video


class VideoCreate(generic.CreateView):
    model = Video
    fields = '__all__'
    success_url = reverse_lazy('videos:video_list')

class VideoDetail(generic.DetailView):
    model = Video
