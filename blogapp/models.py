from django.db import models
from django_markdown.models import MarkdownField
from django.utils import timezone


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = MarkdownField()
    date = models.DateField(null=True, blank=True, default=timezone.now)
    description = models.TextField(blank=True)
    article_type = (
        ('Learning', (
            ('Python', 'python'),
            ('Java', 'java'),
        )
         ),
        ('Life', 'life'),
        ('Other', 'other')
    )
    type = models.CharField(max_length=20, choices=article_type, blank=True)
    lock = models.BooleanField(default=False)
    view_time = models.IntegerField(default=1)
    post_status = models.BooleanField(default=False)
    image_url = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(null=True, blank=True, max_length=20)
    avatar = models.CharField(null=True, blank=True, max_length=40, default="matt")
    comment = models.TextField()
    auto_date = models.DateTimeField(default=timezone.now)
    is_author = models.BooleanField(default=False)
    belong_to = models.ForeignKey(to=Article, related_name="under_comment", null=True, blank=True)
    parent = models.ForeignKey("self", related_name="reply", blank=True, null=True)
    post_myself = models.BooleanField(default=False)
    email = models.EmailField(blank=True)
    has_children = models.BooleanField(default=False)

    def __str__(self):
        return self.name

# for i in Article.objects.all():
#     if i.image_url is "":
#         i.image_url = "http://otr4re8c8.bkt.clouddn.com/sky.png"
#         i.save()
#     print(i.image_url)
