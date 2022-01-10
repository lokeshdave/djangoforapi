from django.db import models

# create the table here
class employe(models.Model):
    id = models.AutoField
    first_name = models.CharField(max_length=255,null=True)
    last_name = models.CharField(max_length=255,null=True)
    company_name = models.CharField(max_length=255,null=True)
    city = models.CharField(max_length=255,null=True)
    state = models.CharField(max_length=255,null=True)
    zip = models.IntegerField(null=True)
    email = models.CharField(max_length=255)
    web = models.CharField(max_length=255)
    age = models.IntegerField(null=True)
    
    def __str__(self):
        return str(self.id)


# Create your models here.
