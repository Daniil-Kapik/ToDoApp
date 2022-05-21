from django.db import models

class User(models.Model):
    first_name = models.CharField(verbose_name="Имя", max_length=64)
    last_name = models.CharField(verbose_name="Фамилия", max_length=64)
    birthday_year = models.PositiveIntegerField(verbose_name="Дата рожд", blank=True)
    email = models.EmailField(verbose_name="ел. почта", max_length=164)