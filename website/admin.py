from django.contrib import admin
from .models import Whoweare

# Register your models here.
@admin.register(Whoweare)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('content',)