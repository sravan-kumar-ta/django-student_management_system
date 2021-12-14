from django.urls import path
from student_management_app import views, HodViews

urlpatterns = [
    path('demo/', views.demo, name="demo"),
    path('', views.showLoginPage, name='login'),
    path('doLogin/', views.doLogin, name="doLogin"),
    path('admin_home/', HodViews.admin_home, name="admin_home"),
    path('add_staff/', HodViews.add_staff, name="add_staff"),
    path('add_staff_save/', HodViews.add_staff_save, name="add_staff_save"),
    path('add_course/', HodViews.add_course, name="add_course"),
    path('add_course_save/', HodViews.add_course_save ,name="add_course_save"),
]
