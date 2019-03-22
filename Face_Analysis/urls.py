from django.conf.urls import url, patterns

urlpatterns = patterns('Face_Analysis.views',
    url(r'^get_photos/', 'get_photos'),
    url(r'^face_analysis/', 'face_analysis'),
                       )
