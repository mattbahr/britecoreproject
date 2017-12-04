from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^risktype/(?P<risktype_name>[A-Z, a-z]+)/$', views.risktype, name='risktype'),
]
