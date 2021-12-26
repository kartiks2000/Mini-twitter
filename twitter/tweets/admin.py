from django.contrib import admin

from .models import Tweet


class Tweetsearch(admin.ModelAdmin):

    search_fields = ['user__username','user__email','content']

    class Meta:
        model = Tweet

admin.site.register(Tweet,Tweetsearch)
