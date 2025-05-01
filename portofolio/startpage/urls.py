from django.urls import path
from . import views

app_name = 'startpage'

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('blog/', views.blog, name='blog'),
    path('cv/', views.cv, name='cv'),
    path('contact/', views.contact, name='contact'),
    path('404/', views.error_404_view, name='error_404'),
]