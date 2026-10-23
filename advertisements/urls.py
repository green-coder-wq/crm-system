from django.urls import path, re_path
from . import views

app_name = 'advertisements'

urlpatterns = [
    path('', views.AdvertisementListView.as_view(), name='list'),
    path('new', views.AdvertisementCreateView.as_view(), name='create'),
    path('statistic', views.AdvertisementStatisticView.as_view(), name='statistic'),
    path('<int:pk>', views.AdvertisementDetailView.as_view(), name='detail'),
    re_path(r'^(?P<pk>\d+)/edit/?$', views.AdvertisementUpdateView.as_view(), name='edit'),
    re_path(r'^(?P<pk>\d+)/delete/?$', views.AdvertisementDeleteView.as_view(), name='delete'),
]
