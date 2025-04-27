from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home-alt/', views.home_alt, name='home_alt'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('pricing/', views.pricing, name='pricing'),
    path('team/', views.team, name='team'),
    path('faq/', views.faq, name='faq'),
    path('services/', views.services_list_view, name='services_list'),
    path('services/<slug:slug>/', views.service_detail_view, name='service_detail'),
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('contact/', views.contact, name='contact'),
]
