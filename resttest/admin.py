from django.contrib import admin
from .models import Game,Probe,Ss,Album,Track



class SS_ext(admin.ModelAdmin):
    list_display = ('name','id')
admin.site.register(Ss,SS_ext)


admin.site.register(Game)
admin.site.register(Probe)

admin.site.register(Album)
admin.site.register(Track)

