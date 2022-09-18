"""Views for attendance tracker"""
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render

from django.views import View
from .models import Person, Meeting, AttendanceRecord

# Create your views here.
class RegisterMemberView(View):
    """Registers/Updates a member's data in the database"""

    def get(self, request):
        """Simple http response"""
        return HttpResponse("Hello, you shouldn't be seeing this right now :)")

    def post(self, request, *args, **kwargs):
        """Handles a post request to the member view"""
        snowflake = request.POST['snowflake']
        full_name = request.POST['full_name']
        email = request.POST['email']
        user = Person.objects.get_or_create(snowflake=snowflake)
        user.full_name = full_name
        user.email = email
        user.save()
        return HttpResponse(status = 200)
        
class TakeAttendanceView(View):
    """A view for a member's  attendance"""
    def post(self, request, announcement_snowflake, user_snowflake):
        """Handles the creation of an attendance record."""
        person = Person.objects.get(snowflake=user_snowflake)
        meeting = Meeting.objects.get(announcement_snowflake=announcement_snowflake)

        record = AttendanceRecord.objects.create(person=person, meeting=meeting)
        record.save()
        return HttpResponse(status = 200)

    def get(self, request, announcement_snowflake, user_snowflake):
        person = Person.objects.get(snowflake=user_snowflake)
        meeting = Meeting.objects.get(announcement_snowflake=announcement_snowflake)
        records = AttendanceRecord.objects.filter(person=person, meeting=meeting)

        if records.count < 1:
            return Http404()


        return JsonResponse(records.first())

class SearchForMemberView(View,):
    """Search for a member based on the first name given"""
