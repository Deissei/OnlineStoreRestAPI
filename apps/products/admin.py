from django.contrib import admin

from apps.products.models import ImageProduct, Product

admin.site.register(ImageProduct)
admin.site.register(Product)