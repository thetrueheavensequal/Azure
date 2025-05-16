from django.urls import path
from home import views as home_views
from . import views
urlpatterns = [
    path('', views.base,name='base'),
    path('home/', home_views.home,name='home'),
    path('signup/', views.signup,name='signup'),
    path('login/', views.login,name='login'),
    path('logout/', views.logout,name='logout'),
]