from django.contrib import admin

from .models import BookModel, Genre, Rating

admin.site.register(BookModel)
admin.site.register(Rating)
admin.site.register(Genre)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'addition')
    search_fields = ('title', 'author')


class GenreAdmin(admin.ModelAdmin):
    list_display = ('title',)


class RatingAdmin(admin.ModelAdmin):
    list_display = ('rating',)
