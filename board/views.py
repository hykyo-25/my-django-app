from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.db import models

from .models import Thread, Comment
from .forms import CommentForm, ThreadForm

# Create your views here.

class IndexView(generic.ListView):
    template_name = "board/index.html"
    context_object_name = 'threads'

    def get_queryset(self):
        """Return the last five published questions."""
        return Thread.objects.order_by('th_date')[:5]

def CreateThread(request):

    if request.method == "POST":
        if request.POST["text"]:
            Thread.objects.create(th_text=request.POST["text"])
            return redirect('board:index')
        else:
            threads = Thread.objects.order_by('th_date')[:5]
            context = {
            'threads': threads,
            'error': "コメントがありません。",
            }
            return render(request, 'board/index.html', context )

class DetailView(generic.DetailView):
    template_name = "board/detail.html"
    model = Thread

def CreateCommennt(request, pk):
    thread = get_object_or_404(Thread, pk=pk)

    if request.method == "POST":
        if request.POST["text"]:
            Comment.objects.create(comm_text=request.POST["text"], thread=thread)
            return redirect('board:detail', pk=pk)
        else:
            context = {
            'thread':thread,
            'error': "コメントがありません。",
            }
            return render(request, 'board/detail.html', context)
