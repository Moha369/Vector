
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('register/', views.register, name = 'register'),
    path('profile/', views.profile, name = 'user_dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name = 'members/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'members/logout.html'), name = 'logout'),
    path('contact/', views.contact, name = 'contact'),
    path('members/', views.members, name = 'members'),
    path('members/<username>', views.user_url, name = 'user_profile'),
    path('about/', views.about, name = 'about')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
