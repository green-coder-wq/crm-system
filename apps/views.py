from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product
from .forms import ProductForm


class ProductListView(ListView):
    model = Product
    template_name = 'products-list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products-detail.html'
    context_object_name = 'object'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products-create.html'
    success_url = reverse_lazy('products:list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products-edit.html'
    success_url = reverse_lazy('products:list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products-delete.html'
    success_url = reverse_lazy('products:list')
