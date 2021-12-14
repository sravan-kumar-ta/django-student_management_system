from django.urls import path
from student_management_app import views, HodViews

urlpatterns = [
    path('demo/', views.demo, name="demo"),
    path('', views.showLoginPage, name='login'),
    path('doLogin/', views.doLogin, name="doLogin"),
]
