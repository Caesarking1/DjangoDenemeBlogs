# Generated by Django 3.2.8 on 2021-11-19 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(max_length=200, verbose_name='İçerik'),
        ),
    ]
