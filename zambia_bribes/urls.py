from django.contrib import admin
from django.urls import path
from reports import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('report/', views.report_bribe, name='report_bribe'),
    path('cases/', views.bribes_list, name='bribes_list'),
    path('info/', views.info, name='info'),
    path('contact/', views.contact_view, name='contact'),
    path("contact/success/", views.contact_success, name="contact_success"),
]
