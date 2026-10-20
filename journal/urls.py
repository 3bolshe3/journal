from django.urls import path
from journal import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('contacts/', views.contact_view, name='contacts'),
    path('about/', views.about_view, name='about'),
    path('students/', views.student_view, name='students'),
    path('groups/', views.groups_view, name='groups'),
    path('groups/<int:group_id>/', views.group_detail_view, name='group_detail'),
]