from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Count
from .models import Advertisement
from .forms import AdvertisementForm


class AdvertisementListView(ListView):
    model = Advertisement
    template_name = 'ads-list.html'
    context_object_name = 'ads'


class AdvertisementDetailView(DetailView):
    model = Advertisement
    template_name = 'ads-detail.html'
    context_object_name = 'object'


class AdvertisementCreateView(CreateView):
    model = Advertisement
    form_class = AdvertisementForm
    template_name = 'ads-create.html'
    success_url = reverse_lazy('advertisements:list')


class AdvertisementUpdateView(UpdateView):
    model = Advertisement
    form_class = AdvertisementForm
    template_name = 'ads-edit.html'
    success_url = reverse_lazy('advertisements:list')


class AdvertisementDeleteView(DeleteView):
    model = Advertisement
    template_name = 'ads-delete.html'
    success_url = reverse_lazy('advertisements:list')


class AdvertisementStatisticView(ListView):
    model = Advertisement
    template_name = 'ads-statistic.html'
    context_object_name = 'ads'

    def get_queryset(self):
        # Аннотируем количество лидов и активных клиентов
        return Advertisement.objects.annotate(
            leads_count=Count('lead', distinct=True),
            customers_count=Count('lead__customer', distinct=True),
        )
