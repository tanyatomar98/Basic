from django.db import models
from django.db.models.fields import CharField
from django.urls import reverse

# Create your models here.

class Article(models.Model):
    title    = models.CharField(max_length=200, null=False, blank=False, default="Human Rights")
    topic    = models.CharField(max_length=100, null=False, blank=False, default="Human Rights")
    words    = models.IntegerField(null=False, blank=False, default=400)

    def get_absolute_url(self):
        return reverse("blog:article-detail", kwargs={"id": self.id})

