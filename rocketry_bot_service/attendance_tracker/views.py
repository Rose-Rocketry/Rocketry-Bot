"""Views for attendance tracker"""
from django.http import HttpResponse, Http404, JsonResponse, HttpResponseForbidden, HttpResponseBadRequest
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.views import View
from .models import Person, Meeting, AttendanceRecord, Guild
from .forms import MemberRegistryForm

# Create your views here.
class RegisterMemberView(View):
    """Registers/Updates a member's data in the database"""

    def get(self, request):
        """Simple http response"""
        form = MemberRegistryForm()
        return render(request, 'attendance_tracker/register_member.html', {'form':form})

    def post(self, request, *args, **kwargs):
        """Handles a post request to the member view"""
        form = MemberRegistryForm(request.POST)

        if not form.is_valid():
            print("Invalid form passed")
            return HttpResponseBadRequest()

        print(form.cleaned_data['user'])
        print(form.cleaned_data['password'])
        auth = authenticate(username=form.cleaned_data['user'], password=form.cleaned_data['password'])

        if auth is None:
            print("No such user")
            return render(request,'attendance_tracker/register_member.html', {'form':form})

        snowflake = form.cleaned_data['snowflake']
        full_name = form.cleaned_data['full_name']
        email = form.cleaned_data['email']
        user, _created = Person.objects.get_or_create(snowflake=snowflake)
        user.full_name = full_name
        user.email = email
        user.snowflake = snowflake
        user.save()
        return render(request, 'attendance_tracker/register_member.html', {'form':form})
               
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

class GuildSettingsView(View):
    """Handles Guild Settings set"""
    def get(self, request, guild_snowflake):
        """Returns data"""
        guild = Guild.objects.get(snowflake=guild_snowflake)
        settings = {
            'name':guild.name,
            'active_member_snowflake':guild.active_member_snowflake,
            'aspiring_member_snowflake':guild.aspiring_member_snowflake,
        }
        return JsonResponse(settings)

class SearchForMemberView(View,):
    """Search for a member based on the first name given"""
