from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from .models import Products
from .forms import ProductsForm

# BASE VIEW = View
# Create your views here.
class ProductsMixin(object):
    model = Products

    def get_object(self):
        id = self.kwargs.get("id")
        obj = None
        if id is not None:
            obj = get_object_or_404(Products, id = id)
        return obj

class ProductUpdateView(ProductsMixin, View):
    template_name = 'products_create.html'

    def get(self, request,id=None , *args, **kwargs):
        obj = self.get_object()
        context = {}
        if obj is not None:
            form = ProductsForm(instance=obj)
            context['form'] = form
            context['object'] = obj
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):
        obj = self.get_object()
        context = {}
        if obj is not None:
            form = ProductsForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            context['form'] = form
            context['object'] = obj
        return render(request, self.template_name, context)
            

class ProductCreateView(View):
    template_name = 'products_create.html'

    def get(self, request, *args, **kwargs):
        form = ProductsForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = ProductsForm(request.POST)
        if form.is_valid():
            form.save()
        context = {"form" : form}
        return render(request, self.template_name, context)


class ProductListView(View):
    template_name = 'products_list.html'
    queryset = Products.objects.all()

    def get(self, request, *args, **kwargs):
        context = {
            'object_list': self.queryset
        }
        return render(request, self.template_name, context)

class MyView(View):
    template_name = 'about.html'
    def get(self ,request,id=None, *args, **kwargs):
        context = {}
        if id is not None:
            obj = get_object_or_404(Products, id=id)
            context['object'] = obj
        return render(request, self.template_name , context)


def my_view(request, *args, **kwargs):
    return render(request, 'about.html', {})