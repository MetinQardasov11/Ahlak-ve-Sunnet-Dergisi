from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import dynamic_page_view
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('', include('base.urls', namespace='base')),
    path('rosetta/', include('rosetta.urls')),
    path('makaleler/', include('blog.urls', namespace='blog')),
    path('playlist/', include('video.urls', namespace='video')),
    path('hizmetler/', include('service.urls', namespace='service')),
    path('iletisim/', include('contact.urls', namespace='contact')),
    path('api/', include('video.api.urls')),
    path('<slug:slug>/', dynamic_page_view, name='dynamic_page'),
    prefix_default_language=False,
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)