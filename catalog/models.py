from django.db import models

# Create your models here.

class Category(models.Model):
    """ Модель категорий товаров. """

    name = models.CharField(
        max_length=100,
        verbose_name='Наименование',
        help_text='Введите наименование категории'
    )
    description = models.TextField(
        verbose_name='Описание категории',
        help_text='Введите описание категории',
        blank=True,
        null=True
    )

    def __str__(self):
        """ Метод стокового представления модели """
        return self.name

    class Meta:
        """ Метаданные модели Category """
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['name',]


class Product(models.Model):
    """ Модель Товара. """
    name = models.CharField(
        max_length=100,
        verbose_name='Наименование',
        help_text='Введите наименование товара'
    )
    description = models.TextField(
        verbose_name='Описание товара',
        help_text='Введите описание товара',
        blank=True,
        null=True
    )
    image = models.ImageField(
        upload_to='image/',
        blank=True,
        null=True,
        verbose_name='Фото',
        help_text='Загрузите фото собаки'
    )
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        help_text='Введите категорию товара',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='category'
    )
    price = models.FloatField(
        verbose_name='Цена',
        help_text='Введите стоимость товара'
    )
    created_at = models.DateField(
        auto_now_add=True
    )
    updated_at = models.DateField(
        auto_now= True
    )

    def __str__(self):
        """ Метод стокового представления модели """
        return f'{self.name} - {self.price}'

    class Meta:
        """ Метаданные модели Product"""
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['name', 'price',]
