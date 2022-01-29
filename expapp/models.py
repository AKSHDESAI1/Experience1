from django.db import models

# Create your models here.
class uploadDocument(models.Model):
    files= models.FileField(upload_to='files')
    date_time = models.DateField(auto_now=True)

