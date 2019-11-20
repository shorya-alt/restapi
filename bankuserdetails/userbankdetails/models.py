from django.db import models

# Create your models here.
class Bank(models.Model):
    ifsc = models.CharField(max_length=11)  # branch
    bank_id = models.BigIntegerField(max_length=50)
    branch = models.CharField(max_length=80)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=30)
    bank_name = models.CharField(max_length=50,null=True)

    def __str__(self):
        return f"{self.ifsc},{self.bank_id},{self.branch},{self.address},{self.city},{self.district},{self.state}"

