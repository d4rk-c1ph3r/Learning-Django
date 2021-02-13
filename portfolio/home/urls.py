from django.contrib import admin
from django.urls import path,include
from . import views

# Django admin Header Customization
admin.site.site_header='D4rk-c1ph3r'
admin.site.site_title='Admin | D4rk-c1ph3r'
admin.site.index_title='Welcome to D4rk-c1ph3r Devloper Administration'

#UrlConf
urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('projects',views.projects,name='project')    
]
