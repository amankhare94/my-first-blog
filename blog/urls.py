from django.conf.urls import url
from . import views


urlpatterns = [
    url('post/list/', views.post_list, name='post_list'),
    url('post/new/', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url('', views.post_list, name='post_list'),
]

print (urlpatterns)
