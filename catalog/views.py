from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from catalog.forms import ProductForm, ProductModeratorForm, AdminForm
from catalog.models import Product


class ProductListView(ListView):
    model = Product


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products_list')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products_list')

    def get_success_url(self):
        return reverse_lazy('catalog:products_detail', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактировать продукт'
        return context

    def get_form_class(self):
        user = self.request.user
        if user.is_superuser or user.is_staff:
            return AdminForm
        elif user.has_perm('catalog.can_unpublish_product'):
            return ProductModeratorForm
        else:
            return ProductForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products_list')

    def get_form_class(self):
        user = self.request.user
        if user.is_superuser or user.is_staff:
            return AdminForm
        elif user.has_perm('catalog.can_unpublish_product') or user == self.object.owner:
            return ProductModeratorForm
        else:
            return ProductForm
        raise PermissionDenied



class HomeTemplateView(TemplateView):
    template_name = "catalog/home.html"


class ContactsTemplateView(TemplateView):
    template_name = "catalog/contacts.html"
