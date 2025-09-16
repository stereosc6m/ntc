from django.urls import path

from . import views

app_name = 'contacts'

urlpatterns = [
    path('', views.contacts, name='contacts'),
    path('request-form/', views.create_request, name='create_request')
]