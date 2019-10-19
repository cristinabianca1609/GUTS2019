# from food_waste_project.food_waste_management_app.models import *
import datetime

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food_waste_project.settings')


import django
django.setup()

# from food_waste_project.food_waste_management_app.models import User, Barcode, UserProduct
from food_waste_management_app.models import *


def add_user(d):
    user = User()
    user.new_user(d)
    user.save()


def add_barcode(d):
    bar = Barcode()
    bar.new_barcode(d)
    bar.save()


def add_product(d):
    p = UserProduct()
    p.add_product(d)
    p.save()


user1 = {'username': 'lenka', 'password': 'a'}
user2 = {'username': 'cristina', 'password': 'a'}
user3 = {'username': 'patrick', 'password': 'a'}

b1 = {'barcode_no': 56353635632, 'name': 'sticks'}
b2 = {'barcode_no': 643, 'name': 'trees'}

p1 = {'user_id': 1, 'barcode_no': 7622210863362, 'exp_date': datetime.datetime.utcnow() + datetime.timedelta(days=3)}
p2 = {'user_id': 1, 'barcode_no': 5000168180083, 'exp_date': datetime.datetime.utcnow() + datetime.timedelta(days=3)}

#add_user(user1)
#add_user(user2)
#add_user(user3)

#add_barcode(b1)
#add_barcode(b2)

#add_product(p1)
#add_product(p2)


def runner():
    #add_user(user1)
    #add_user(user2)
    #add_user(user3)

    add_barcode(b1)
    add_barcode(b2)

    #add_product(p1)
    #add_product(p2)


if __name__ == '__main__':
    print("populating script!")
    runner()
