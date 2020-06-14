from django.contrib import admin

from .models import BookModel, Genre, Rating

admin.site.register(BookModel)
admin.site.register(Genre)
admin.site.register(Rating)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'addition')
    search_fields = ('title', 'author')


class GenreAdmin(admin.ModelAdmin):
    list_display = ('title',)


class RatingAdmin(admin.ModelAdmin):
    list_display = ('rating',)
