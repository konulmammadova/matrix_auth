from django.conf.urls import url
from account import views
from django.contrib.auth.views import logout

urlpatterns = [
    # url(r'^$', views.login, name="login"),
    url(r'^logout/$', logout, name="logout", kwargs={'next_page': '/'}),
    url(r'^register/$', views.register, name="register"),
    url(r'^$', views.hello, name="hello"),
    url(r'^data/$', views.insert_db, name="add"),
]
