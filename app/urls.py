from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserListView.as_view(), name='user_list'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
    path('users/add/', views.UserCreateView.as_view(), name='user_add'),
    path('users/<int:pk>/edit/', views.UserUpdateView.as_view(), name='user_edit'),
    path('users/<int:pk>/delete/', views.UserDeleteView.as_view(), name='user_delete'),

    path('caregivers/', views.CaregiverListView.as_view(), name='caregiver_list'),
    path('caregivers/<int:pk>/', views.CaregiverDetailView.as_view(), name='caregiver_detail'),
    path('caregivers/add/', views.CaregiverCreateView.as_view(), name='caregiver_add'),
    path('caregivers/<int:pk>/edit/', views.CaregiverUpdateView.as_view(), name='caregiver_edit'),
    path('caregivers/<int:pk>/delete/', views.CaregiverDeleteView.as_view(), name='caregiver_delete'),

    path('members/', views.MemberListView.as_view(), name='member_list'),
    path('members/<int:pk>/', views.MemberDetailView.as_view(), name='member_detail'),
    path('members/add/', views.MemberCreateView.as_view(), name='member_add'),
    path('members/<int:pk>/edit/', views.MemberUpdateView.as_view(), name='member_edit'),
    path('members/<int:pk>/delete/', views.MemberDeleteView.as_view(), name='member_delete'),

    path('addresses/', views.AddressListView.as_view(), name='address_list'),
    path('addresses/<int:pk>/', views.AddressDetailView.as_view(), name='address_detail'),
    path('addresses/add/', views.AddressCreateView.as_view(), name='address_add'),
    path('addresses/<int:pk>/edit/', views.AddressUpdateView.as_view(), name='address_edit'),
    path('addresses/<int:pk>/delete/', views.AddressDeleteView.as_view(), name='address_delete'),

    path('jobs/', views.JobListView.as_view(), name='job_list'),
    path('jobs/<int:pk>/', views.JobDetailView.as_view(), name='job_detail'),
    path('jobs/add/', views.JobCreateView.as_view(), name='job_add'),
    path('jobs/<int:pk>/edit/', views.JobUpdateView.as_view(), name='job_edit'),
    path('jobs/<int:pk>/delete/', views.JobDeleteView.as_view(), name='job_delete'),

    path('jobapplications/', views.JobApplicationListView.as_view(), name='jobapplication_list'),
    path('jobapplications/<int:pk>/', views.JobApplicationDetailView.as_view(), name='jobapplication_detail'),
    path('jobapplications/add/', views.JobApplicationCreateView.as_view(), name='jobapplication_add'),
    path('jobapplications/<int:pk>/edit/', views.JobApplicationUpdateView.as_view(), name='jobapplication_edit'),
    path('jobapplications/<int:pk>/delete/', views.JobApplicationDeleteView.as_view(), name='jobapplication_delete'),

    path('appointments/', views.AppointmentListView.as_view(), name='appointment_list'),
    path('appointments/<int:pk>/', views.AppointmentDetailView.as_view(), name='appointment_detail'),
    path('appointments/add/', views.AppointmentCreateView.as_view(), name='appointment_add'),
    path('appointments/<int:pk>/edit/', views.AppointmentUpdateView.as_view(), name='appointment_edit'),
    path('appointments/<int:pk>/delete/', views.AppointmentDeleteView.as_view(), name='appointment_delete'),
]
