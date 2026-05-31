from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import contacts, product_detail, product_add
from catalog.views import HomeListView

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', HomeListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('product_add/', product_add, name='product_add'),
]