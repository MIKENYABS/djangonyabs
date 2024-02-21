from django.contrib import admin
from django.urls import path
from hostelapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='homepage'),
    path('about/', views.aboutus, name='about'),
    path('about/', views.aboutus),
    path('form/', views.form,name = 'formpage'),

]

