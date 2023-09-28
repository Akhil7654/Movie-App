from django.db import models

# Create your models here.

class movie(models.Model):
    img=models.ImageField(upload_to="img_movie")
    name=models.CharField(max_length=250)
    gen=models.CharField(max_length=250)
    year=models.IntegerField()
    des=models.TextField()

    def __str__(self):
        return self.name
