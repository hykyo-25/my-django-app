from django.db import models
from django.utils import timezone

# Create your models here.

class Thread(models.Model):
    th_text = models.CharField(max_length=30)
    th_date = models.DateTimeField(default=timezone.now)
    th_comm_cnt = models.IntegerField(default=0)

    def __str__(self):
        return self.th_text

class Comment(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    comm_text = models.CharField(max_length=100)
    comm_date = models.DateTimeField(default=timezone.now)
    comm_like = models.IntegerField(default=0)

    def __str__(self):
        return self.comm_text
