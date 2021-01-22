from django.urls import path
from Data_Page import views
from django.contrib import admin
from django.conf.urls import url

urlpatterns = [
   path('', views.Data_Page, name='Data_Page'),
   path('summary', views.summary, name = 'summary'),
   path('details', views.details, name = 'details')
  # path("details", ProjectListView.as_view())
]

