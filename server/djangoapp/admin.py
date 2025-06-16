from django.contrib import admin
from .models import CarMake, CarModel

# Register your models here.

# Registering models with their respective admins
# admin.site.register(CarMake)
# admin.site.register(CarModel)


@admin.register(CarMake)
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ("name", "car_make", "type", "year")
    list_filter = ("car_make", "type", "year")
    search_fields = ("name",)

    def get_readonly_fields(self, request, obj=None):
        # If the listing is imported, make some fields readonly to avoid accidental edits
        if obj and obj.is_imported:
            return self.readonly_fields + ("price", "car_model")
        return self.readonly_fields


# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here
