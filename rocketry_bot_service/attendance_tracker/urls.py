from django.urls import path

from . import views

urlpatterns = [
    path('update_member/', views.RegisterMemberView.as_view(), name='register_update_member'),
    path('mentions_by_first_name/', views.SearchForMemberView.as_view(), name='member_search'),
    path('record_attendance/<slug:announcement_snowflake>/<slug:user_snowflake>', views.TakeAttendanceView.as_view(), name='take_attendance'),
]
