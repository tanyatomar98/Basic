from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.urls import reverse
from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

# Create your views here.

# def article_create_view(request, *args, **kwargs):
#     my_form = ArticleForm(request.POST or None)
#     if my_form.is_valid():
#         my_form.save()
#         my_form = ArticleForm()
#     context = {
#         'form' : my_form
#     }
#     return render(request, 'Article/article_create.html', context)

class ArticleCreateView(CreateView):
    template_name = 'Article/article_create.html'
    form_class = ArticleForm
    queryset = Article.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

# def article_detail_view(request, id, *args, **kwargs):
#     # object = Article.objects.get(id=id)
#     object = get_object_or_404(Article, id=id)
#     context = {
#         'object' : object
#     }
#     return render(request, 'Article/article_detail.html', context)

class ArticleDetailView(DetailView):
    template_name = "Article/article_detail.html"
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)
    

class ArticleListView(ListView):
    template_name = 'Article/article_list.html'
    queryset = Article.objects.all()
    
class ArticleUpdateView(UpdateView):
    template_name = 'article/article_create.html'
    form_class = ArticleForm
    queryset = Article.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

class ArticleDeleteView(DeleteView):
    template_name = 'article/article_delete.html'
    # queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)
    
    def get_success_url(self):
        return reverse("blog:article-list")
