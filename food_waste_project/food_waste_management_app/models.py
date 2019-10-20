from django.contrib.auth.models import User
from django.db import models

class UserProfileInfo(models.Model):
    # user_id = models.IntegerField(primary_key=True, unique=True, null=False, auto_created=True)
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.user.username


class Barcode(models.Model):
    barcode_id = models.IntegerField(primary_key=True, unique=True, null=False, auto_created=True)
    barcode_no = models.TextField(unique=True, null=False, auto_created=True)
    product_name = models.TextField(null=False)
    url = models.URLField()

    def new_barcode(self, barcode_info):
        self.barcode_no = barcode_info['barcode_no']
        self.product_name = barcode_info['name']
        # if 'url' in barcode_info:
        #     self.url = barcode_info['url']


class UserProduct(models.Model):
    user_product_id = models.IntegerField(primary_key=True, unique=True, null=False, auto_created=True)
    exp_date = models.DateField(null=False)

    barcode = models.ForeignKey(Barcode, on_delete=models.CASCADE)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def add_product(self, product, username):
        self.barcode_no = product['barcode_no']
        self.exp_date = product['exp_date']

        bar = Barcode.objects.filter(barcode_no = product['barcode_no'])[0]
        self.barcode = bar

        user_obj = User.objects.filter(username = username)[0]
        self.user = user_obj





