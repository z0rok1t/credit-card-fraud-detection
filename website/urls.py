from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('data', views.data, name='data'),
    path('home1', views.home1, name='home1'),
    path('prediction', views.prediction, name='prediction'),
    path('results', views.results, name='results'),
    path('login/', views.login_user, name='login'),
    path('signup/', views.signup_user, name='signup'),
    path('logout/', views.logout_user, name='logout'),
      
]