from django.conf.urls import patterns, include, url
from django.contrib import admin
#from audio_uploader.views import ProfileImageView, ProfileDetailView
from django.conf.urls.static import static


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'starter.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', 'login.views.login_user'),
    url(r'^audio/$', 'audio_uploader.views.add_audio'),
	url(r'^php/upload.php', 'upload.php'),)
#	url(r'^upload/', ProfileImageView.as_view(), name='profile_image_upload'),
#    url(r'^uploaded/(?P<pk>\d+)/$', ProfileDetailView.as_view(),
#        name='profile_image'),
#	) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
