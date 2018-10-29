from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('thuvienbk/', include('thuvienbk.urls')),
    path('admin/', admin.site.urls),
]
