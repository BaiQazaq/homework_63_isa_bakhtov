from django.contrib import admin

# Register your models here.
from posts.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("id","image", "description", "author", "created_at")
    list_filter = ("id", "image", "description", "author")
    search_fields = ("author", "created_at")
    fields = ("image", "description", "author")
    readonly_fields = ("id", "created_at", "changed_at")

admin.site.register(Post, PostAdmin)