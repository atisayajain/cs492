from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [

	# admin/
    url(r'^admin/', admin.site.urls),

    # accounts/
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),

    # home/
    url(r'^home/', include('home.urls', namespace='home')),

    # api/postings/
    url(r'^api/postings/', include('api.urls', namespace='api-postings')),

]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)