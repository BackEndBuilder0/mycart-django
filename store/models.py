from audioop import reverse

from django.db import models
from category.models import Category
from django.urls import reverse


# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, unique=True)
    price = models.IntegerField()
    product_img = models.ImageField(upload_to='images/product')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_link(self):
        return reverse('product_by_productslug', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name


