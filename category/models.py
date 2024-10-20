from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to='images/category')

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_links(self):
        return reverse('product_by_category', args=[self.slug])

    def __str__(self):
        return self.category_name