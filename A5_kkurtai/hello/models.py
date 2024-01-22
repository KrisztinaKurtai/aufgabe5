from django.db import models
from django.utils import timezone

class Users(models.Model):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class LogMessage(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"