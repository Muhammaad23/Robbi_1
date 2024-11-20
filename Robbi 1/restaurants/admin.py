from django.contrib import admin
from .models import *

# Customize the admin interface for Restaurants
@admin.register(Restaurants)
class RestaurantsAdmin(admin.ModelAdmin):
    list_display = ('title', 'jop_time', 'address')  # Fields to display in the admin list view
    search_fields = ('title', 'address')            # Fields to enable search
    list_filter = ('jop_time',)                     # Fields to enable filtering

# Customize the admin interface for Restaurant_info
@admin.register(Restaurant_info)
class RestaurantInfoAdmin(admin.ModelAdmin):
    list_display = ('address', 'tel', 'latitude', 'longitude')  # Fields to display in the admin list view
    search_fields = ('address', 'tel')                         # Fields to enable search
    list_filter = ('latitude', 'longitude')                    # Fields to enable filtering

# Customize the admin interface for Menu
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')            # Fields to display in the admin list view
    search_fields = ('title',)                   # Fields to enable search
    list_filter = ('price',)                     # Fields to enable filtering
