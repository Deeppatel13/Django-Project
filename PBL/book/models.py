from django.db import models

class BookForm(models.Model):
    pickup_location = models.CharField(max_length=250)
    drop_location = models.CharField(max_length=250)
    mobile_no = models.CharField(max_length=10)
    username = models.CharField(max_length=100)
    email= models.EmailField()
    