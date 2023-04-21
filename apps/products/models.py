from django.db import models



class ImageProduct(models.Model):
    image = models.ImageField(upload_to='product/')


class Product(models.Model):
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category')
    title = models.CharField(max_length=155)
    description = models.TextField(max_length=600)
    created_at = models.DateTimeField(auto_now_add=True)

    images = models.ManyToManyField(ImageProduct)

    def __str__(self):
        return self.title