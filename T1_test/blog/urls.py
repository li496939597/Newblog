from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'blog'

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$',views.index,name="index"),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
]