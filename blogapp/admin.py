from django.contrib import admin
from .models import Article, Comment
from pagedown.widgets import AdminPagedownWidget
from django import forms

# Register your models here.
class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget=AdminPagedownWidget) #和数据库的名字保持一致

class AriticleAdmin(admin.ModelAdmin):
    form = ArticleForm

admin.site.register(Article, AriticleAdmin)
admin.site.register(Comment)