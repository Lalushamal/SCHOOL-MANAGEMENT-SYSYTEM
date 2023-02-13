from django.urls import path
from . import views

urlpatterns= [
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('register',views.register, name='register'),
    path('course',views.course,name='course'),
    path('attendence',views.attendence,name='attendence'),
    path('mark',views.mark,name='mark'),
    path('view/<int:view_id>/',views.view,name='view'),
    path('student',views.student,name='student'),
    path('delete/<int:view_id>/', views.delete, name='delete'),
    path('edit/<int:view_id>/', views.edit, name='edit'),
    path('getpdf',views.getpdf,name='getpdf'),
    path('pdf/',views.pdf_view,name='pdf_view'),
    path('attend/',views.attend,name='attend'),
]