from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models
import hashlib
import bcrypt

class User(models.Model):
    user_id = models.IntegerField(primary_key=True, unique=True, null=False, auto_created=True)
    username = models.TextField(unique=True, null=False)
    salt = models.TextField(null=False)
    password = models.TextField(null=False)

    def new_user(self, user_info):
        self.username = user_info['username']
        salt = bcrypt.gensalt()
        self.salt = salt
        self.password = hashlib.pbkdf2_hmac('sha256', user_info['password'].encode, salt.encode(), 100000)


class UserProduct(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, null=False, auto_created=True)
    barcode_no = models.IntegerField(null=False)
    exp_date = models.DateField(null=False)
    product_name = models.TextField(null=False)

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def add_product(self, product):
        self.barcode_no = product['barcode_no']
        self.exp_date = product['exp_date']
        # self.product_name = Barcode.product_name

    def delete_product(self, product):
        pass


class Barcode(models.Model):
    barcode_id = models.IntegerField(primary_key=True, unique=True, null=False, auto_created=True)
    barcode_no = models.IntegerField(unique=True, null=False, auto_created=True)
    product_name = models.TextField(null=False)

    def new_barcode(self, barcode_info):
        self.barcode_no = barcode_info['barcode_no']
        self.product_name = barcode_info['name']
