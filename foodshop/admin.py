from django.contrib import admin
from.models import *
# Register your models here.

class catadmin(admin.ModelAdmin):
    prepopulated_fields ={'slug':('name',)}
admin.site.register(categ,catadmin)
class prodAdmin(admin.ModelAdmin):
    list_display = ['name','slug','price','img','stock']
    list_editable = ['price','img','stock']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(products,prodAdmin)