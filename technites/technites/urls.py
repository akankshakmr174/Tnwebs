from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from technites import settings
from technites.views import home
from technites.views2 import particle
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^home/', home),
    url(r'^particle/', particle),
    url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^gallery/', include('galeria.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
 
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

