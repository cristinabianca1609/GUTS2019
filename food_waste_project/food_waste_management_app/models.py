from django.db import models
from django.contrib.auth.models import User

# Create your models here.
import hashlib
import bcrypt

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.user.username

# class User(models.Model):
#     user_id = models.IntegerField(primary_key=True, unique=True, null=False, auto_created=True)
#     username = models.TextField(unique=True, null=False)
#     password = models.TextField(null=False)
#
#     def new_user(self, user_info):
#         self.username = user_info['username']
#         self.password =user_info['password']


class Barcode(models.Model):
    barcode_id = models.IntegerField(primary_key=True, unique=True, null=False, auto_created=True)
    barcode_no = models.TextField(unique=True, null=False, auto_created=True)
    product_name = models.TextField(null=False)
    url = models.URLField()

    def new_barcode(self, barcode_info):
        self.barcode_no = barcode_info['barcode_no']
        self.product_name = barcode_info['name']
        if 'url' in barcode_info:
            self.url = barcode_info['url']


class UserProduct(models.Model):
    user_product_id = models.IntegerField(primary_key=True, unique=True, null=False, auto_created=True)
    barcode_no = models.IntegerField(null=False)
    product_name = models.TextField(null=False)
    exp_date = models.DateField(null=False)


    def add_product(self, product):
        self.barcode_no = product['barcode_no']
        self.exp_date = product['exp_date']
        self.product_name = product['product_name']
        # self.product_name = Barcode.product_name

    # def delete_product(self, product_name):
    #     self.objects.filter(self.product_name == product_name).delete()
    #     pass
