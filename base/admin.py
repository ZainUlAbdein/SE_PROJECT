from django.contrib import admin
from .models import Song, Book

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ['book_file', "name", "user", "created_at"]
    search_fields = ["name"]


admin.site.register(Song)
admin.site.register(Book, BookAdmin)
