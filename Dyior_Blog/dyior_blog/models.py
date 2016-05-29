from __future__ import unicode_literals

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
    html_content = models.TextField(editable=False)
    author = models.ForeignKey(User)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    created = models.DateTimeField(default=datetime.datetime.now())
    modified = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        ordering = ['modified']
        verbose_name_plural = "articles"

    @permalink
    def get_absolute_url(self):
        return "blog-article", (), {'slug': self.slug}

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


class PhotoAlbum(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

    @permalink
    def get_absolute_url(self):
        return 'photoalbum_detail', None, {'object_id': self.id}


class Photo(models.Model):
    title = models.CharField(max_length=20)
    album = models.ForeignKey(PhotoAlbum)
    image = models.ImageField(upload_to='photos')
    caption = models.TextField()

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

    @permalink
    def get_absolute_url(self):
        return 'photo_detail', None, {'object_id': self.id}


class PhotoInline(admin.TabularInline):
    model = Photo


class PhotoAlbumAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]


admin.site.register(PhotoAlbum, PhotoAlbumAdmin)
admin.site.register(Photo)


class MusicAlbum(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

    @permalink
    def get_absolute_url(self):
        return 'musicalbum_detail', None, {'object_id': self.id}


class Music(models.Model):
    title = models.CharField(max_length=20)
    album = models.ForeignKey(PhotoAlbum)
    song = models.FileField(upload_to='music')
    caption = models.TextField()

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

    @permalink
    def get_absolute_url(self):
        return 'music_detail', None, {'object_id': self.id}


class MusicInline(admin.TabularInline):
    model = Music


class MusicAlbumAdmin(admin.ModelAdmin):
    inlines = [MusicInline]


admin.site.register(MusicAlbum, MusicAlbumAdmin)
admin.site.register(Music)


class UrlAlbum(models.Model):
    tag = models.CharField(max_length=20)
    description = models.TextField()

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

    @permalink
    def get_absolute_url(self):
        return 'urlalbum_detail', None, {'object_id': self.id}


class Url(models.Model):
    title = models.CharField(max_length=20)
    album = models.ForeignKey(UrlAlbum)
    url = models.URLField(null=True, blank=True)
    caption = models.TextField()

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

    @permalink
    def get_absolute_url(self):
        return 'url_detail', None, {'object_id': self.id}


class UrlInline(admin.TabularInline):
    model = Music


class UrlAlbumAdmin(admin.ModelAdmin):
    inlines = [MusicInline]


admin.site.register(UrlAlbum, UrlAlbumAdmin)
admin.site.register(Url)
