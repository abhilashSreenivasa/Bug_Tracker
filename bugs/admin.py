from django.contrib import admin
from bugs.models import Bug,BugType,BugPriority,BugStatus,BugHistory

# Register your models here.
admin.site.register(Bug)
admin.site.register(BugType)
admin.site.register(BugPriority)
admin.site.register(BugStatus)
admin.site.register(BugHistory)



