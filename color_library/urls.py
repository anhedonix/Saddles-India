from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.color_list, name='color_home'),
    url(r'^color_library', views.color_list, name='color_list'),
]
