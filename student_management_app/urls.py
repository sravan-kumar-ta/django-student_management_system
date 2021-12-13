from django.urls import path
from student_management_app import views

urlpatterns = [
    path('', views.demo, name="demo"),
    path('login/', views.showLoginPage, name='login'),
    path('doLogin/', views.doLogin, name="doLogin"),
]