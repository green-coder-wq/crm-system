from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Lead
from .forms import LeadForm


class LeadListView(ListView):
    model = Lead
    template_name = 'leads-list.html'
    context_object_name = 'leads'


class LeadDetailView(DetailView):
    model = Lead
    template_name = 'leads-detail.html'
    context_object_name = 'object'


class LeadCreateView(CreateView):
    model = Lead
    form_class = LeadForm
    template_name = 'leads-create.html'
    success_url = reverse_lazy('leads:list')


class LeadUpdateView(UpdateView):
    model = Lead
    form_class = LeadForm
    template_name = 'leads-edit.html'
    success_url = reverse_lazy('leads:list')


class LeadDeleteView(DeleteView):
    model = Lead
    template_name = 'leads-delete.html'
    success_url = reverse_lazy('leads:list')
