from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home,name='home'),
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('booking/', views.booking,name='booking'),
    path('events/', views.event_types, name='events'),
    path('status/', views.status,name='status'),
    path('login/', views.login,name='login'),
    path('signup/', views.signup,name='signup'),
    path('logout/', views.logout,name='logout'),
    path('profile/', views.profile, name='profile'),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
