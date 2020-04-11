from django.db import models
from django.shortcuts import reverse
from datetime import datetime


class BookModel(models.Model):
    title = models.CharField(max_length=50, db_index=True,
                             verbose_name="Название книги")
    author = models.CharField(
        max_length=50, db_index=True, verbose_name="Автор")
    dateline = models.CharField(
        max_length=100, verbose_name="Издательство и год выпуска")
    genre = models.ManyToManyField(
        'Genre', related_name='book', verbose_name="Раздел")
    addition = models.CharField(max_length=1000, verbose_name="Описание")
    rating = models.ManyToManyField(
        'Rating', related_name='book', verbose_name="Рейтинг")
    slug = models.SlugField(max_length=50, blank=True, unique=True)
    time_added = models.DateTimeField(default=datetime.now())

    def get_absolute_url(self):
        return reverse('book_details_url', kwargs={'slug': self.slug})
    #  попробовать использовать функцию в дальнейшем

    def get_update_url(self):
        return reverse('book_update_form', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = self.author + '_' + self.title
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Библиотека'
        verbose_name_plural = 'Библиотека'
        ordering = ['-time_added']


class Genre(models.Model):
    title = models.CharField(max_length=50, db_index=True,
                             verbose_name="Название жанра")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Жанр'


class Rating(models.Model):
    rating = models.CharField(
        max_length=15, db_index=True, verbose_name="Оценка")

    def __str__(self):
        return self.rating

    class Meta:
        verbose_name_plural = 'Рейтинг'
