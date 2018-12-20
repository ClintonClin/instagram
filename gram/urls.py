from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.registration, name='registration'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.confirm, name='confirm'),
    url(r'^user/(?P<username>\w{0,50})', views.profile, name='profile'),
    url(r'^search/', views.profile_search, name='profile_search'),
    url(r'^upload/$', views.pic_upload, name='pic_upload'),
    url(r'^image/(?P<image_id>\d+)', views.solo_image, name='solo_image'),
    url(r'^accounts/edit/', views.profile_edit, name='profile_edit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

