from django.urls import path
from . import views
from .views import LoginView

urlpatterns = [
    path('employees/', views.employee_list),
    path('employees/<int:pk>/', views.employee_detail),
    path('activities/', views.activity_list),
    path('activities/<int:pk>/', views.activity_detail),
    path('auth/login/', LoginView.as_view(), name='login')
]
