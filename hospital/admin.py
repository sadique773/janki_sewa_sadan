from django.contrib import admin
from .models import Doctor, Gallery




@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("name", "specialization", "created_at")

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("id", "photo", "created_at")