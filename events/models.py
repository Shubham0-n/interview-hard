from django.db import models
from users.models import CustomUser


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100, null=True, blank=False)
    description = models.TextField(max_length=500, null=True, blank=True)
    start_time = models.DateTimeField(null=True, blank=False)
    end_time = models.DateTimeField(null=True, blank=False)
    location = models.CharField(max_length=200, blank=False, null=True)
    owner = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, null=True, blank=False
    )

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"


class Attendee(models.Model):
    attendee = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Attendee"
        verbose_name_plural = "Attendees"


class Session(models.Model):
    title = models.CharField(max_length=50, null=True, blank=False)
    start_time = models.DateField(null=True, blank=False)
    end_time = models.DateField(null=True, blank=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Session"
        verbose_name_plural = "Sessions"
