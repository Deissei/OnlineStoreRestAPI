from django.db import models
from django.urls import reverse
from apps.users.models import StoreUser

from apps.categories.models import Category


class ImageProduct(models.Model):
    title = models.CharField(max_length=10, null=True, blank=True)
    image = models.ImageField(upload_to='product/')


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category')
    title = models.CharField(max_length=155)
    description = models.TextField(max_length=600)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    images = models.ManyToManyField(ImageProduct, related_name='images_product', blank=True)

    slug = models.SlugField(unique=True)
    manufacturer = models.ForeignKey(StoreUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})


    class Meta:
        ordering = ('title', )
    