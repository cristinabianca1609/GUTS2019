# from food_waste_project.food_waste_management_app.models import *
import datetime

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food_waste_project.settings')

import django

django.setup()

# from food_waste_project.food_waste_management_app.models import User, Barcode, UserProduct
from food_waste_management_app.models import User, UserProduct, Barcode


# User.objects.all().delete()
# UserProduct.objects.all().delete()
Barcode.objects.all().delete()


def add_barcode(d):
    bar = Barcode()
    bar.new_barcode(d)
    bar.save()


def add_product(d, username):
    p = UserProduct()
    p.add_product(d, username)
    print (p)
    p.save()

def add_user(d):
    u = User()
    u.username=d['username']
    u.password = d['password']
    u.save

# real 7622210863362   5000168180083
p1 = {'barcode_no': '0000000000178', 'exp_date': datetime.datetime.utcnow() + datetime.timedelta(days=3)}
p2 = {'barcode_no': '0000000000123', 'exp_date': datetime.datetime.utcnow() + datetime.timedelta(days=3)}
p3 = {'barcode_no': '0000000000017', 'exp_date': datetime.datetime.utcnow() + datetime.timedelta(days=3)}

u1 = {'username': 'lenka', 'password':'a'}
u2 = {'username': 'cristina', 'password':'a'}
u3 = {'username': 'patryk', 'password':'a'}



def populate_barcode():
    with open('generalized_data.csv', 'r') as f:
        for line in f.readlines()[1:]:
            full_line = line.split(';')
            add_barcode({'barcode_no': full_line[0],
                        'name': full_line[2]
                        # 'url':full_line[1]
                             })

def populate_users():
    add_user(u1)
    add_user(u2)
    add_user(u3)

def populate_user_product():
    add_product(p1, 'Lenka')
    # add_product(p2, 'cristina')
    add_product(p3, 'Lenka')


def runner():
    # try:
    #     with open('generalized_data.csv', 'r') as f:
    #         for line in f.readlines()[1:]:
    #             full_line = line.split(';')
    #             add_barcode({'barcode_no': full_line[0],
    #                         'name': full_line[2],
    #                         'url':full_line[1]
    #                              })
    # except:
    #     pass
    #
    # add_product(p1, 'lenka')
    # add_product(p2, 'cristina')
    # add_product(p3, 'lenka')

    populate_barcode()
    # populate_user_product()


if __name__ == '__main__':
    print("populating script!")
    runner()
