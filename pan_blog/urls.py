"""pan_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blogapp.views import blog, blog_content, comment
from blogapp.api import article


urlpatterns = [
    url(r'^$', blog, name="home"),
    url(r'^admin/', admin.site.urls),
    url(r'^blog/(?P<cate>[A-Za-z]+)$', blog, name="cate_filter"),
    url(r'^blog/$', blog, name="blog"),
    url(r'^content/(?P<page_num>\d+)$', blog_content, name="content"),
    url(r'^content/(?P<page_num>\d+)/comment$', comment, name="comment"),
    url(r'^api/article', article)
]
