from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Customer
from .forms import CustomerForm
from leads.models import Lead


class CustomerListView(ListView):
    model = Customer
    template_name = 'customers-list.html'
    context_object_name = 'customers'


class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customers-detail.html'
    context_object_name = 'object'


class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers-create.html'
    success_url = reverse_lazy('customers:list')

    def get_initial(self):
        initial = super().get_initial()
        lead_id = self.request.GET.get('lead_id')
        if lead_id:
            initial['lead'] = get_object_or_404(Lead, pk=lead_id)
        return initial


class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers-edit.html'
    success_url = reverse_lazy('customers:list')


class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customers-delete.html'
    success_url = reverse_lazy('customers:list')
