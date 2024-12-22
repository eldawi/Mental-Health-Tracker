from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_patient/', views.add_patient, name='add_patient'),
    path('add_doctor/', views.add_doctor, name='add_doctor'),
    path('add_user/', views.add_user, name='add_user'),
    path('view_users/', views.view_users, name='view_users'),
    path('register_problem/', views.register_problem, name='register_problem'),
    path('book_therapy_session/', views.book_therapy_session, name='book_therapy_session'),
    path('follow_up/', views.follow_up, name='follow_up'),
    path('consult_doctor/', views.consult_doctor, name='consult_doctor'),
    path('prescribe_medication/', views.prescribe_medication, name='prescribe_medication'),
    path('set_sessions/', views.set_sessions, name='set_sessions'),
]