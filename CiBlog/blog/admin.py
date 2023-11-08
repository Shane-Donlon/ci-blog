from django.contrib import admin
from . import models
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

@admin.register(models.Post)
class PostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("status", "created_on")
    list_display = ("title", "slug", "status", "created_on",)
    search_fields = ["title", "content"]
    summernote_fields = ("content")
    

admin.site.register(models.Comment)