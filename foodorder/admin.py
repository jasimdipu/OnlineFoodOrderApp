from django.contrib import admin
from .models import *


# Register your models here.


class SocialAdmin(admin.ModelAdmin):
    list_display = ['social_name', 'facebook_link', 'tweeter_link', 'instagram_link', 'linkedin_link']
    search_fields = ['social_name', 'facebook_link', 'tweeter_link', 'instagram_link', 'linkedin_link']


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'middle_name', 'last_name', 'email']
    search_fields = ['first_name', 'last_name', 'email']


class MarchentAdmin(admin.ModelAdmin):
    list_display = ['Owner_name', 'no_of_res', 'email', 'phone', 'reg_date', 'validation_date']
    search_fields = ['Owner_name', 'last_name', 'email', 'phone']
    list_filter = ['reg_date', 'validation_date']


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['res_name', 'mar_id', 'email', 'phone', 'lic_validity_date', 'res_validation_date']
    search_fields = ['Owner_name', 'last_name', 'email', 'phone']
    list_filter = ['lic_validity_date', 'res_validation_date']


admin.site.register(Socialmedia, SocialAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Marchent, MarchentAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
