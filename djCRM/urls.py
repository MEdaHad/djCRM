from django.contrib import admin
from django.urls import path

from core.views import index, about

urlpatterns = [
    path('', index, name="index"),
    path('about/ ', about, name="about"),
    path('admin/', admin.site.urls),
]
