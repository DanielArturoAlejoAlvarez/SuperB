from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^details/(?P<id>\w{0,50})/$', views.details),
    url(r'^details/(?P<slug>[-\w]+)/$', views.details),     
    url(r'^category/(?P<id>\w+)/$', views.category, name='category'),    
    url(r'^tag/(?P<id>\w{0,50})/(?P<slug>[-\w]+)/$', views.tag, name='tag'),
]