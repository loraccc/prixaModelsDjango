from django.contrib import admin
from django.urls import path,include
from debug_toolbar import urls as dt_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('models/',include('modelType.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
]
