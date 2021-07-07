from django.urls import path

from . import views

app_name = 'board'

urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('create_thread/', views.CreateThread, name='create_thread'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/create_comment/', views.CreateCommennt, name='create_comment'),
]
