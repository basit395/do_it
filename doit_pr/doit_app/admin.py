from django.contrib import admin

from .models import Task, Player

#admin.site.register(Task)
#admin.site.register(Player)



class TaskAdmin(admin.ModelAdmin):
    list_display = ('description','task_age')
    ordering = ('description',)
    search_fields = ('description',)

admin.site.register(Task, TaskAdmin)
