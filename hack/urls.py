from django.conf.urls import url
from hack import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
]