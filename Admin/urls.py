from django.conf.urls import url, patterns

urlpatterns = patterns('Admin.views',
    url(r'^add_user/', 'add_user'),
    url(r'^login/', 'loginn'),
    url(r'^personal/', 'personal'),
    url(r'^admin/', 'admin'),



                       ),