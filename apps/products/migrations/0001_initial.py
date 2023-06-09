# Generated by Django 4.2 on 2023-04-21 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product/')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155)),
                ('description', models.TextField(max_length=600)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_product', to='products.imageproduct')),
            ],
        ),
    ]
