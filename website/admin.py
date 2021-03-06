from django.contrib import admin
from .models import Whoweare,Contact,Ourhistory

# Register your models here.
@admin.register(Whoweare)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('content',)

@admin.register(Ourhistory)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('description',)
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'comentario')
    list_filter = ('email',)
    search_fields = ('email',)



