from django.db import models


# Create your models here.
class Img(models.Model):
    img_id = models.AutoField(primary_key=True)
    img_url = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'img'
