from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Product


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products_list')

    def get_success_url(self):
        return reverse_lazy('catalog:products_detail', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактировать продукт'
        return context


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('dogs:products_list')


class HomeTemplateView(TemplateView):
    template_name = "catalog/home.html"


class ContactsTemplateView(TemplateView):
    template_name = "catalog/contacts.html"
