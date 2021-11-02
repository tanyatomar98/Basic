from django.contrib import admin
from django.urls import path
from .views import MyView, ProductUpdateView , my_view, ProductListView, ProductCreateView

app_name = 'products'
urlpatterns = [
    path('', MyView.as_view(template_name="contact.html"), name='my-view'),
    path('<int:id>', MyView.as_view(template_name='products_detail.html'), name='products-detail'),
    path('list/', ProductListView.as_view(), name='products-list'),
    path('create/', ProductCreateView.as_view(), name='products-create'),
    path('<int:id>/update', ProductUpdateView.as_view(), name="products-update")
    # path('', my_view, name='new-view')
]
