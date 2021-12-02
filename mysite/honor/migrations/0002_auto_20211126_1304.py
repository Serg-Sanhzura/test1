# Generated by Django 3.2.9 on 2021-11-26 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('honor', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='honor',
            options={'verbose_name': 'Дошка пошани', 'verbose_name_plural': 'Занести на дошку пошани'},
        ),
        migrations.AlterField(
            model_name='honor',
            name='content',
            field=models.TextField(blank=True, verbose_name='Стисла автобіографія'),
        ),
        migrations.AlterField(
            model_name='honor',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опоблікування на дошку'),
        ),
        migrations.AlterField(
            model_name='honor',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Ім`я'),
        ),
        migrations.AlterField(
            model_name='honor',
            name='photo',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото співробітника'),
        ),
        migrations.AlterField(
            model_name='honor',
            name='position',
            field=models.CharField(max_length=150, verbose_name='Посада'),
        ),
        migrations.AlterField(
            model_name='honor',
            name='rank',
            field=models.CharField(max_length=50, verbose_name='Звання'),
        ),
        migrations.AlterField(
            model_name='honor',
            name='surname',
            field=models.CharField(max_length=20, verbose_name='Прізвище'),
        ),
    ]
