from django.contrib import admin
from .models import Hotels

class HotelsAdmin(admin.ModelAdmin):
    list_display = ('title', 'job_time', 'address', 'star_rating')
    search_fields = ('title', 'address')
    list_filter = ('star_rating',)

admin.site.register(Hotels, HotelsAdmin)
