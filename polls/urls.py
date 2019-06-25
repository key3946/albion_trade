from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('rank/', views.rank, name='rank'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('license/', views.license_, name='license'),
    path('renew/<str:redirect>/', views.renew, name='renew'),
    path('price/<str:unique_name>', views.price, name='price'),
    path('profit_all/<str:from_city>/<str:to_city>', views.profit_all, name='profit_all'),
    path('profit_item/<str:unique_name>/<str:from_city>/<str:to_city>', views.profit_item, name='profit_item'),
]
