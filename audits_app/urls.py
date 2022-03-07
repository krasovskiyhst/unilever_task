from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.index, name='index'),
    path('create_audit/', views.create_audit, name='create_audit'),
    path('list_of_audits/', views.list_of_audits, name='list_of_audits'),
    path('edit_audit/<audit_id>/', views.edit_audit, name='edit_audit'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('logout', views.logout_view, name='logout'),
]
