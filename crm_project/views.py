from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from products.models import Product
from advertisements.models import Advertisement
from leads.models import Lead
from customers.models import Customer


@login_required
def index_view(request):
    context = {
        'products_count': Product.objects.count(),
        'advertisements_count': Advertisement.objects.count(),
        'leads_count': Lead.objects.count(),
        'customers_count': Customer.objects.count(),
    }
    return render(request, 'index.html', context)
