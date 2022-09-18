"""Models for tracking attendance"""
from django.db import models
import django

# Create your models here.
class Person(models.Model):
    """A model for a person in the club."""
    ACTIVE_STATUSES = (
        ('A', 'Active'),
        ('B', 'Aspiring'),
    )
    full_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    active_status = models.CharField(max_length=1, choices=ACTIVE_STATUSES, default="B")
    snowflake = models.CharField(max_length=32, unique=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.full_name

class Meeting(models.Model):
    """A model for a meeting """
    name = models.CharField(max_length=60)
    date = models.DateTimeField()
    duration = models.DurationField()
    announcement_snowflake = models.CharField(max_length=32)
    message = models.CharField(max_length=1000)

class AttendanceRecord(models.Model):
    """A model for an attendance record."""
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    last_updated = models.DateTimeField(default=django.utils.timezone.now)

class Guild(models.Model):
    """A model for storing Guild settings"""
    