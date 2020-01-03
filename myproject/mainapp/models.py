from django.db import models

# Create your models here.
class uploaded(models.Model):
    charfield=models.CharField(max_length=1000)
    filefield=models.FileField(upload_to='')