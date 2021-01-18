from django.db import models

class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

class book(models.Model):
    title=models.CharField(max_length=255, verbose_name='Заголовок')
    subtitle=models.CharField(max_length=100, verbose_name='Подзаголовок')
    description=models.TextField(max_length=650, verbose_name='Описание')
    price=models.IntegerField(verbose_name='Цена')
    genre=models.CharField(max_length=50, verbose_name='Жанр')
    author=models.CharField(max_length=40, verbose_name='Автор')
    year=models.DateField(verbose_name='Год выхода книги')
    data=models.DateField(auto_now_add=True, verbose_name='Добавление книги на сайт')

    class Meta:
        verbose_name = 'Книжный магазин'
        verbose_name_plural = 'Книжные магазины'

