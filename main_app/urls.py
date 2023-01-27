from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pythons/', views.pythons_index, name='index'),
    path('pythons/<int:python_id>/', views.pythons_detail, name='detail'),
    path('pythons/create/', views.PythonCreate.as_view(), name='pythons_create')
]