from django.db import models
from django.urls import reverse

# Create your models here.
class Products(models.Model):
    title  = models.CharField(max_length=100, null= False, blank=False)

    def get_absolute_url(self):
        return reverse('products:products-detail', kwargs={"id":self.id})