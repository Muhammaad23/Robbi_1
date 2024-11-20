from django.contrib import admin
from .models import *

class Hotel_informationAdmin(admin.ModelAdmin):
    list_display = ('title', 'job_time', 'address', 'star_rating')
    search_fields = ('title', 'address')
    list_filter = ('star_rating',)

admin.site.register(Hotel_information, Hotel_informationAdmin)


class HotelsAdmin(admin.ModelAdmin):
    list_display = ('title', 'job_time', 'address', 'image')  # Fields to display in the admin list view
    search_fields = ('title', 'address')  # Fields to search in the admin panel
    list_filter = ('job_time',)  # Add filter options for job_time
    ordering = ('title',)  # Order the list by the 'title' field
    readonly_fields = ('id',)  # Make the 'id' field read-only in the admin

admin.site.register(Hotels, HotelsAdmin)

