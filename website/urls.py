from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('data', views.data, name='data'),
    path('home1', views.upload_dataset, name='home1'),
    path('login/', views.login_user, name='login'),
    path('signup/', views.signup_user, name='signup'),
    path('logout/', views.logout_user, name='logout'),
    path('prediction/', views.prediction,name='prediction'),
    path('results/', views.results,name='results')
    
    
]