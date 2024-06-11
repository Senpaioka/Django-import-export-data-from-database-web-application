from django.contrib import admin
from main_site.models import StudentModel, CustomerID, UploadModel

# Register your models here.

admin.site.register(StudentModel)
admin.site.register(CustomerID)
admin.site.register(UploadModel)