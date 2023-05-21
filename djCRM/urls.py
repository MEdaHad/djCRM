from django.contrib import admin
from django.contrib.auth import views
from django.urls import path,include

from core.views import index, about
from userprofile.views import signup

urlpatterns = [
    path('', index, name="index"),
    path('dashboard/leads/', include('lead.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('sign-up/', signup, name="signup"),
    path('log-in/', views.LoginView.as_view(template_name='userprofile/login.html'), name="login"),
    path('log-out/', views.LogoutView.as_view(), name="logout"),
    path('about/ ', about, name="about"),
    path('admin/', admin.site.urls),
]
