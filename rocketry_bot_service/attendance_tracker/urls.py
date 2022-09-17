from django.urls import path

from . import views

urlpatterns = [
    path('update_member/', views.RegisterMemberView.as_view(), name='register_update_member'),
]
