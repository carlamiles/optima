from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r'^$', views.show_registration),
    url(r'^login$', views.show_login),
    url(r'^process_login$', views.process_login),
    url(r'^register_user$', views.register_user),
    url(r'^logout$', views.logout),
    url(r'^my_account/(?P<user_id>\w+)$', views.show_account),
    url(r'^update_account/(?P<user_id>\w+)$', views.update_account),
]