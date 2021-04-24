from django.db import models


class Data(models.Model):
    key=models.CharField(max_length=256, unique=True)
    data=models.CharField(max_length=256)
