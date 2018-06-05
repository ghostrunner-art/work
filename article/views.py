from django.shortcuts import render_to_response,get_object_or_404
from django.http import HttpResponse
from .models import Article

def article_detail(request,article_id):

    article = get_object_or_404(Article,id =article_id)
    context = dict()
    context['article_obj'] = article
    return render_to_response('article_detail.html',context)

def article_list(request):
    articles = Article.objects.filter(is_deleted= False)
    context = dict()
    context['articles'] = articles
    return render_to_response('article_list.html', context)

def index(request):
    return HttpResponse('hellos world')
# Create your views here.
