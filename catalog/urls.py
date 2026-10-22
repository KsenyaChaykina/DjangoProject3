from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ContactsTemplateView, HomeTemplateView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path("products/", ProductListView.as_view(), name='products_list'),
    path("products/<int:pk>/", ProductDetailView.as_view(), name='products_detail'),
    path('products/create/', ProductCreateView.as_view(), name='products_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='products_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='products_delete'),

    path("contacts/", ContactsTemplateView.as_view(), name='contacts'),
    path("home/", HomeTemplateView.as_view(), name='home'),
]
