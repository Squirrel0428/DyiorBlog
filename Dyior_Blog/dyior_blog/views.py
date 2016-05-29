from django.shortcuts import render_to_response, RequestContext
from models import Article


def article_list(request):
    articles = Article.objects.order_by('-id').all()
    return render_to_response('list.html', {'articles': articles}, context_instance=RequestContext(request))


def article_view(request, id):
    article = Article.objects.get(id=id)
    return render_to_response('view.html', {'article': article},
                              context_instance=RequestContext(request))


def photo_list(request):
    articles = Article.objects.order_by('-id').all()
    return render_to_response('list.html', {'articles': articles}, context_instance=RequestContext(request))


def photo_view(request, id):
    article = Article.objects.get(id=id)
    return render_to_response('view.html', {'article': article},
                              context_instance=RequestContext(request))


def music_list(request):
    articles = Article.objects.order_by('-id').all()
    return render_to_response('list.html', {'articles': articles}, context_instance=RequestContext(request))


def music_view(request, id):
    article = Article.objects.get(id=id)
    return render_to_response('view.html', {'article': article},
                              context_instance=RequestContext(request))


def url_list(request):
    articles = Article.objects.order_by('-id').all()
    return render_to_response('list.html', {'articles': articles}, context_instance=RequestContext(request))


def url_view(request, id):
    article = Article.objects.get(id=id)
    return render_to_response('view.html', {'article': article},
                              context_instance=RequestContext(request))