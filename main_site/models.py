from django.db import models

# Create your models here.

class StudentModel(models.Model):
    roll_no = models.IntegerField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    
    
class CustomerID(models.Model):
    customer_name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.customer_name


class UploadModel(models.Model):
    file_name = models.FileField(upload_to='uploads/')
    upload_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name.name
    