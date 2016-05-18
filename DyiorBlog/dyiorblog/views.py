from django.shortcuts import render_to_response, RequestContext, get_object_or_404
from models import Category, Tag, Article, Comment
from django.db.models import Q


def list(request):
    articles = Article.objects.order_by('-id').all()
    return render_to_response('list.html', {'articles': articles}, context_instance=RequestContext(request))


def view(request, id):
    article = Article.objects.get(id=id)
    comments = Comment.objects.filter(Article=id).order_by("id").all()
    print len(comments)
    return render_to_response('view.html', {'article': article, 'comments': comments}, context_instance=RequestContext(request))


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    article_list = Article.objects.filter(category=category)
    heading = "Category: %s" % category.label
    return render_to_response("list.html", locals())


def search(request):
    if 'q' in request.GET:
        term = request .GET['q']
        article = Article.objects.filter(Q(title_contains) | Q(markdown_content_contains=term))
        heading = "Search results"
    return render_to_response("list.html", locals())
