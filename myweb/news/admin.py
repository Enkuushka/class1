from django.contrib import admin

from .models import Medee, LikeCounter

admin.site.register(Medee)
admin.site.register(LikeCounter)