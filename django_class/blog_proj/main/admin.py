from django.contrib import admin
from .models import Post
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "status","created")
    list_filter = ("status", "created", "publish")
    list_editable = ("status",)
    search_fields = ("title", "slug", "body")
    date_hierarchy = "publish"
    search_help_text = "Search for posts your have created."
    prepopulated_fields = {'slug': ('title',)}
    
    
