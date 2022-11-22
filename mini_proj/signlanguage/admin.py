from django.contrib import admin

# Register your models here.
from .models import *

# 관리에서 Result 객체에 대해  기본 CRUD 관리를 한다. 
admin.site.register(Result)
admin.site.register(ai_admin)
class ai_admin(admin.ModelAdmin) :
    list_display = ("id", "file", "checkbox", "input_count", "correct_count")
    ordering = ("-created_at", ) 