from django.contrib import admin
from users.models import User
from . import models


admin.site.register(User)
admin.site.register(models.LogMessage)