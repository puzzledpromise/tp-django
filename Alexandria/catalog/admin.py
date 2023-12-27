from django.contrib import admin

from catalog.models import Book, Author

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'birth_year')



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author_last_name')
    list_filter = ('author', )

    def author_last_name(self, obj):
        return obj.author.last_name