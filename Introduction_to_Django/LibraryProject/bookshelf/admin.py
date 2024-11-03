from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to display
    search_fields = ('title', 'author')  # Fields to be searchable
    list_filter = ('publication_year',)  # Filters for the sidebar

# Register your models here.
admin.site.register(Book, BookAdmin)

