from django.db import models

# Create your models here.

class DocumentModel(models.Model):
    title=models.CharField( max_length=150,null=True)
    Document = models.FileField(upload_to='documents/%Y/%m/%d')