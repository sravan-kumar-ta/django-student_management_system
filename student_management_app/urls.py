from django.urls import path
from student_management_app import views, HodViews, StudentViews, StaffViews

urlpatterns = [
    path('demo/', views.demo, name="demo"),
    path('', views.showLoginPage, name='show_login'),
    path('doLogin/', views.doLogin, name="do_login"),
    path('admin_home/', HodViews.admin_home, name="admin_home"),
    # path('', HodViews.admin_home, name="admin_home"),

    path('logout_user/', views.logout_user, name="logout"),
    path('add_staff/', HodViews.add_staff, name="add_staff"),
    path('add_staff_save/', HodViews.add_staff_save, name="add_staff_save"),
    path('add_course/', HodViews.add_course, name="add_course"),
    path('add_course_save/', HodViews.add_course_save, name="add_course_save"),
    path('add_student/', HodViews.add_student, name="add_student"),
    path('add_student_save/', HodViews.add_student_save, name="add_student_save"),
    path('add_subject/', HodViews.add_subject, name="add_subject"),
    path('add_subject_save/', HodViews.add_subject_save, name="add_subject_save"),
    path('manage_staff/', HodViews.manage_staff, name="manage_staff"),
    path('manage_student/', HodViews.manage_student, name="manage_student"),
    path('manage_course/', HodViews.manage_course, name="manage_course"),
    path('manage_subject/', HodViews.manage_subject, name="manage_subject"),
    path('edit_staff/<str:staff_id>/', HodViews.edit_staff, name="edit_staff"),
    path('edit_staff_save/', HodViews.edit_staff_save, name="edit_staff_save"),
    path('edit_student/<str:student_id>/', HodViews.edit_student, name="edit_student"),
    path('edit_student_save/', HodViews.edit_student_save, name="edit_student_save"),
    path('edit_subject/<str:subject_id>/', HodViews.edit_subject, name="edit_subject"),
    path('edit_subject_save/', HodViews.edit_subject_save, name="edit_subject_save"),
    path('edit_course/<str:course_id>/', HodViews.edit_course, name="edit_course"),
    path('edit_course_save/', HodViews.edit_course_save, name="edit_course_save"),
    path('manage_session', HodViews.manage_session, name="manage_session"),
    path('add_session_save', HodViews.add_session_save, name="add_session_save"),

    # Staff URL Path  <------------->
    path('staff_home/', StaffViews.staff_home, name="staff_home"),
    path('staff_take_attendance/', StaffViews.staff_take_attendance, name="staff_take_attendance"),
    path('get_students', StaffViews.get_students, name="get_students"),
    path('save_attendance_data', StaffViews.save_attendance_data, name="save_attendance_data"),

    path('student_home/', StudentViews.student_home, name="student_home"),
]
