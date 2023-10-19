from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField()
    slug = models.SlugField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="product_images")

    def __str__(self):
        return self.name
