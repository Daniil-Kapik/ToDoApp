# Generated by Django 4.0.4 on 2022-05-21 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=64, verbose_name='Фамилия')),
                ('birthday_year', models.PositiveIntegerField(blank=True, verbose_name='Дата рожд')),
                ('email', models.EmailField(max_length=164, verbose_name='ел. почта')),
            ],
        ),
    ]