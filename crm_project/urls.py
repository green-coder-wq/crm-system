from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('', login_required(TemplateView.as_view(template_name='index.html')), name='index'),
    
    path('products/', include('products.urls')),
    path('ads/', include('advertisements.urls')),
    path('leads/', include('leads.urls')),
    path('contracts/', include('contracts.urls')),
    path('customers/', include('customers.urls')),
]
