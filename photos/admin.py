from django.contrib import admin
from .models import Category,Photo
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','category']

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id','category','image','dec']