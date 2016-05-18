from django.conf.urls import *
from models import Article

info_dict = {'queryset': Article.objects.all(), 'template_object_name': 'article'}


urlpatterns = patterns('django.views.generic.list',
        url(r'^(?P<slug>[-\w]+)/$', 'ListView', info_dict, name="blog-article"),
        url(r'^$', 'ListView', info_dict, name="blog-home"),
)


urlpatterns += patterns('dyiorblog.views',
        url(r'^category/(?P<slug>[-\w]+)/$', 'category', name="blog-category"),
        url(r'^search/$', 'search', name="blog-search"),
)
