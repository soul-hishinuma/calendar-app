from django.db import models

# Create your models here.

class EventsModel(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    # event_type = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.event_name
