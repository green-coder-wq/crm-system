from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Contract
from .forms import ContractForm


class ContractListView(ListView):
    model = Contract
    template_name = 'contracts-list.html'
    context_object_name = 'contracts'


class ContractDetailView(DetailView):
    model = Contract
    template_name = 'contracts-detail.html'
    context_object_name = 'object'


class ContractCreateView(CreateView):
    model = Contract
    form_class = ContractForm
    template_name = 'contracts-create.html'
    success_url = reverse_lazy('contracts:list')


class ContractUpdateView(UpdateView):
    model = Contract
    form_class = ContractForm
    template_name = 'contracts-edit.html'
    success_url = reverse_lazy('contracts:list')


class ContractDeleteView(DeleteView):
    model = Contract
    template_name = 'contracts-delete.html'
    success_url = reverse_lazy('contracts:list')
