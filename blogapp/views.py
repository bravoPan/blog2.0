from django.shortcuts import render, redirect
from .models import Article, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blogapp.forms import CommentForm
from django.utils import timezone


# Create your views here.


def blog(request, cate=None):
    check_time_zone()
    context = {}
    article_type = ["Python", "Java", "Life", "Other"]
    if cate is None:
        content = Article.objects.all()
    else:
        if cate.capitalize() in article_type:
            content = Article.objects.filter(type=cate.capitalize())
        else:
            content = Article.objects.all()
    page_robot = Paginator(content.order_by("-date"), 4)
    page_num = request.GET.get("page")
    try:
        article_list = page_robot.page(page_num)
    except EmptyPage:
        article_list = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        article_list = page_robot.page(1)
    context['article_list'] = article_list
    return render(request, 'blog_home.html', context)


def blog_content(request, page_num, error_form=None):
    context = {}
    form = CommentForm
    view_update = Article.objects.get(id=page_num)
    view_update.view_time += 1
    view_update.save()
    context['detail'] = view_update
    comments_for_this_article = Comment.objects.filter(belong_to=view_update)
    comments = comments_for_this_article.filter(parent=None)
    replys = [x for x in comments_for_this_article if x not in comments]
    context['comments'] = comments
    context['replys'] = replys

    if error_form is not None:
        context['form'] = error_form
    else:
        context['form'] = form
    return render(request, 'blog_content.html', context)


def comment(request, page_num):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.cleaned_data["comment"]
        # avatar = form.cleaned_data["avatar"]
        email = form.cleaned_data['email']
        parent_id = form.cleaned_data["parent"]
        # if it is the chilren/parent
        if parent_id:
            parent_model = Comment.objects.get(id=parent_id)
            label_has_chilren(parent_model)
        else:
            parent_model = None
        if request.user.is_authenticated:
            myself = True
            name = "pan"
        else:
            myself = False
            name = form.cleaned_data["name"]
        a = Article.objects.get(id=page_num)
        c = Comment(name=name, comment=comment, belong_to=a, email=email, post_myself=myself, parent=parent_model)
        c.save()
    else:
        return blog_content(request, page_num, error_form=form)
    return redirect(to="content", page_num=page_num)


def label_has_chilren(parent):
    parent.has_children = True
    parent.save()


def check_time_zone():
    for i in Article.objects.all():
        now = timezone.now().date()
        difference = now - i.date
        stander = timezone.timedelta(days=3)
        if difference <= stander:
            i.post_status = True
            i.save()
        else:
            i.post_status = False
            i.save()
