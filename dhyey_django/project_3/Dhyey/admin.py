from django.contrib import admin

# Register your models here.

@admin.register(student)
class studentAdmin(admin.ModelAdmin):
    list_display=['id','name','age','address','email']