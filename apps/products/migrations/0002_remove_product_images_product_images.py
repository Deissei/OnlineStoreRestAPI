# Generated by Django 4.2 on 2023-04-22 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='images',
        ),
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ManyToManyField(to='products.imageproduct'),
        ),
    ]
