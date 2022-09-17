"""Views for attendance tracker"""
from django.http import HttpResponse
from django.shortcuts import render

from django.views import View
from .models import Person

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
        user = Person.objects.filter(snowflake=snowflake).first()
        if user is None:
            user = Person.objects.create(full_name=full_name, email=email, snowflake=snowflake)
        else:
            user.full_name = full_name
            user.email = email
        user.save()
        return HttpResponse(status = 200)
        
class TakeAttendanceView(View):
    """A view for a member's  attendance"""
    def post(self, request, *args, **kwargs):
        """Handles the creation of an attendance record."""
