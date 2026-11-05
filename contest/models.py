from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator

class Contest(models.Model):
    title = models.CharField('Название', max_length=20)
    description = models.TextField('Описание')
    price = models.IntegerField('Рекомендованная розничная цена', validators=[MinValueValidator(10), MaxValueValidator(100)])
    comment = models.TextField('Комментарий')