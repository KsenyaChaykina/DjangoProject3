from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ContactsTemplateView, HomeTemplateView

app_name = CatalogConfig.name

urlpatterns = [
    path("products/", ProductListView.as_view(), name='products_list'),
    path("products/<int:pk>/", ProductDetailView.as_view(), name='products_detail'),
    path("contacts/", ContactsTemplateView.as_view(), name='contacts'),
    path("home/", HomeTemplateView.as_view(), name='home'),
]
