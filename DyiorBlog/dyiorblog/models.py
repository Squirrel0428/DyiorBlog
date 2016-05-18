import datetime
from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User
from django.contrib import admin
from markdown import markdown


VIEWABLE_STATUS = [3, 4]


class ViewableManager(models.Manager):
    def get_query_set(self):
        default_queryset = super(ViewableManager, self).get_query_set()
        return default_queryset.filter(status__in=VIEWABLE_STATUS)


class Category(models.Model):
    label = models.CharField(blank=True, max_length=16)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'categories'

    def __unicode__(self):
        return self.label


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('label',)}


admin.site.register(Category, CategoryAdmin)


class Tag(models.Model):
    pag = models.CharField(max_length=16)


class Article(models.Model):

    STATUS_CHOICES = (
        (1, "No Permission"),
        (2, "Needs Editor"),
        (3, "Needs Approval"),
        (4, "Published"),
        (5, "Archived"),
        (6, "Record"),
    )

    title = models.CharField(max_length=16)
    slug = models.SlugField()
    category = models.ForeignKey(Category)
    markdown_content = models.TextField()
    html_content = models.TextField()
    author = models.ForeignKey(User)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    created = models.DateTimeField(default=datetime.datetime.now())
    modified = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        ordering = ['modified']
        verbose_name_plural = "articles"

    @permalink
    def get_absolute_url(self):
        return ("blog-article", (), {'slug': self.slug})

    def save(self):
        self.html_content = markdown(self.markdown_content)
        self.modified = datetime.datetime.now()
        super(Article, self).save()

    admin_objects = models.Manager()
    objects = ViewableManager()


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'created', 'modified')
    search_fields = ('title', 'content')
    list_filter = ('status', 'author', 'created', 'modified')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Article, ArticleAdmin)


class Comment(models.Model):
    article = models.ForeignKey(Article)
    content = models.TextField()
    name = models.CharField(max_length=16)
    email = models.EmailField()