from django.db import models
from django.urls import reverse

class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, blank=True, null=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', blank=True, null=True)
    
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"slug": self.slug})
    


    class Meta:
        verbose_name_plural = "Categories"
        ordering = ('title', )
