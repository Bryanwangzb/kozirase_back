from django.urls import path
from . import views

app_name = 'text_analysis_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('',views.index,name='index')
]
