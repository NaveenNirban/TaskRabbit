from django.contrib import admin
from taskbunny.models import OtherProileData,Task
from django.contrib.auth.models import User

# Register your models here.
# admin.site.register(User)
admin.site.register(OtherProileData)
admin.site.register(Task)