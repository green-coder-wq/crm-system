from django.contrib import admin
from django.urls import path, include
from crm_project.views import index_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', index_view, name='index'),
    path('products/', include('products.urls')),
    path('ads/', include('advertisements.urls')),
    path('leads/', include('leads.urls')),
    path('contracts/', include('contracts.urls')),
    path('customers/', include('customers.urls')),
]
