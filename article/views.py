from django.shortcuts import render
from article.models import Article
from django.views import generic
# Create your views here.


def index(request):
    titles = Article.objects.all()
    context = {
        'titles': titles
    }
    return render(request, 'index.html', context=context)


def about(request):

    return render(request, 'about.html')


class ArticleListView(generic.ListView):
    model = Article


class ArticleDetailView(generic.DetailView):
    model = Article
