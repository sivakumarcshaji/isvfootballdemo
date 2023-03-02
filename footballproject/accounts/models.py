from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class User_accounts(models.Model):
    username=models.CharField(max_length=150,unique=True)
    emailid=models.EmailField(unique=True)
    phone_number=PhoneNumberField(unique=True)

    def __str__(self,):
        return self.username

