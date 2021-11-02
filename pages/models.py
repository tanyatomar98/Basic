from django.db import models
from django.urls import reverse

# Create your models here.
class UserName(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse("pages:sign", kwargs={"my_id": self.id})

    def get_delete_user_url(self):
        return reverse("pages:delete-user", kwargs={"my_id": self.id})
    
    
