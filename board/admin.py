from django.contrib import admin

# Register your models here.
from .models import Thread, Comment

class CommentInline(admin.TabularInline):
    model = Comment

class ThreadAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['th_text']}),
        ('Date information', {'fields': ['th_date']})
    ]
    inlines = [CommentInline]

admin.site.register(Thread, ThreadAdmin)
