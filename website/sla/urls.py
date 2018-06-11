from django.conf.urls import url
from . import views #we are importing the views from this folder


app_name = 'sla'

urlpatterns = [
    

    # /sla/
    url(r'^$', views.index, name='index'), #default homepage


    # /sla/<sla_id>/
    url(r'^(?P<sla_id>[0-9]+)/$', views.detail,name='detail'),
    
    # /sla/<sla_id>/terms/<term_id>
    url(r'^(?P<sla_id>[0-9]+)/terms/(?P<term_id>[0-9]+)/$', views.termDetail,name='termDetail'),

]
