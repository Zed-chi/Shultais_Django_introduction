from django.contrib import admin
from houses.models import House


@admin.register(House)
class AdminHouse(admin.ModelAdmin):
    list_display = ["name", "price"]
