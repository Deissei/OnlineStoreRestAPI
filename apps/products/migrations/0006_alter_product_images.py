# Generated by Django 4.2 on 2023-04-24 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_manufacturer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.ManyToManyField(blank=True, null=True, related_name='images_product', to='products.imageproduct'),
        ),
    ]