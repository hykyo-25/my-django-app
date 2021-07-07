from django import forms
from .models import Comment, Thread


class CommentForm(forms.Form):
    name = forms.CharField(label='コメントを入力', max_length=100)

    class Meta:
        model = Comment
        exclude = ('thread', 'comm_date', 'comm_like')

class ThreadForm(forms.Form):
    name = forms.CharField(label='スレッドを入力', max_length=100)

    class Meta:
        model = Thread
        exclude = ('th_date', 'th_comm_cnt')
