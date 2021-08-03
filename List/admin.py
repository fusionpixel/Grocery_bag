from .models import AddItem
from django.contrib import admin

# Register your models here.


class AddItemAdmin(admin.ModelAdmin):
    list_display = ["name", "quantity", "status", "date", "user"]


admin.site.register(AddItem, AddItemAdmin)
