from basket.views import basket
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls'), name='store'),
    path('basket/', include('basket.urls'), name='basket')
]
