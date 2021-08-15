from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('product/', views.product, name='product'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact')
] + staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)