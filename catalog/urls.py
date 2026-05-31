from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import contacts
from catalog.views import HomeListView, ProductAddCreateView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', HomeListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product_add/', ProductAddCreateView.as_view(), name='product_add'),
]