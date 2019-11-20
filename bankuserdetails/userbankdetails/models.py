from django.db import models

# Create your models here.
class Bank(models.Model):
    ifsc = models.CharField(max_length=11,null=True)  
    bank_id = models.IntegerField(null=True)
    branch = models.CharField(max_length=80,null=True)
    address = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=50,null=True)
    district = models.CharField(max_length=50,null=True)
    state = models.CharField(max_length=30,null=True)
    bank_name = models.CharField(max_length=50,null=True)

    #def __str__(self):
        #return f"{self.ifsc},{self.bank_id},{self.branch},{self.address},{self.city},{self.district},{self.state}"

