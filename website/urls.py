from django.urls import path
from . import views

#basically urls are the starting point of our django project
urlpatterns = [
    path('',views.home, name="home"),

    path('contact.html',views.contact, name="contact"),

    path('pricing.html',views.pricing, name="pricing"),

    path('about.html',views.about, name="about"),

    path('blog.html',views.blog,name='blog'),

    path('blog-details.html',views.blog_details,name='blog_details'),

    path('service.html',views.service,name='service'),

    path('table.html',views.table,name='table'),

    path('panel.html',views.panel,name='panel'),
    
    path('delete_event/<id>',views.delete_event,name='delete_data'),

]
