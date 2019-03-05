from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('about/', views.about, name='about'),
    path('about/index', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio_details/', views.portfolio_details, name='portfolio_details')

]
