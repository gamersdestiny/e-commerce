from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<str:slug>', views.product, name='product'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact')
] + staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
