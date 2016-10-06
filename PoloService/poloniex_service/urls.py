from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^public$', views.public_api, name='public_api'),
    url(r'^trading$', views.trading_api, name='trading_api')
]