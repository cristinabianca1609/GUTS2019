from django.contrib import admin
from food_waste_management_app.models import UserProfileInfo, Barcode, UserProduct

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Barcode)
admin.site.register(UserProduct)
