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
# Barcode.objects.all().delete()


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

<<<<<<< Updated upstream

def populate_barcode():
    with open('generalized_data.csv', 'r') as f:
        for line in f.readlines()[1:]:
            full_line = line.split(';')
            add_barcode({'barcode_no': full_line[0],
                        'name': full_line[2],
                        'url':full_line[1]
                             })

def populate_users():
    add_user(u1)
    add_user(u2)
    add_user(u3)

def populate_user_product():
    add_product(p1, 'lenka')
    add_product(p2, 'cristina')
    add_product(p3, 'lenka')


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
    # with open('generalized_data.csv', 'r') as f:
    #     for line in f.readlines()[1:]:
    #         full_line = line.split(';')
    #         add_barcode({'barcode_no': full_line[0],
    #                     'name': full_line[2],
    #                     'url':full_line[1]
    #                          })
    # add_product(p1, 'lenka')
    # add_product(p2, 'cristina')
    # add_product(p3, 'lenka')
    populate_barcode()
    # populate_users()
    populate_user_product()
=======
add_barcode(b1)
add_barcode(b2)

add_product(p1)
add_product(p2)
result =  (Barcode.objects.filter(barcode_no = '0000000000017').values('product_name'))
print (result)

def list_user_products(id):
    result = UserProduct.objects.all().filter(user_id = id)
    product_exp = dict()
    for i in result:

        name = Barcode.objects.filter(barcode_id = i.barcode_id)#.values('product_name')
        product_exp[i.user_product_id] = [name[0].product_name.strip('\n'), i.exp_date]

    return product_exp #dictinary - list value

def get_user_id(username):
    result = User.objects.filter(username = username)[0]
    return result.id        #user_id
def create_barcode(new_bar_dict):
    new_bar = Barcode()
    new_bar.new_barcode(new_bar_dict)

    new_bar.save()

def add_user_product(username):
    product_dict = dict()
    # barcode_info = scan_barcode()
    barcode_info = {'barcode': '123123', 'type': 'EAN13'}
    barcode = barcode_info['barcode']
    #     is in DB?
    try:
        # //TODO: implement the OCR
        product_dict['exp_date'] = datetime.datetime.utcnow()+datetime.timedelta(days=3)
        result = Barcode.objects.filter(barcode_no= barcode)
        product_dict['barcode_no'] = result[0].barcode_no

        new_product = UserProduct()
        new_product.add_product(product_dict, username)
        # user = User.objects.filter(username = username)
        # user.barcode_no = barcode
        new_product.save()
        result = 'done'
    except:
        result = 'does not exist'

    return result


nb = {'barcode_no': '0987654576',
      'name': 'presnidavka'}


def runner():
    try:
        with open('generalized_data.csv', 'r') as f:
            for line in f.readlines()[1:]:
                full_line = line.split(';')
                add_barcode({'barcode_no': full_line[0],
                            'name': full_line[2],
                            'url':full_line[1]
                                 })
    except:
        pass

    add_product(p1, 'lenka')
    add_product(p2, 'cristina')
    add_product(p3, 'lenka')

    list_user_products(get_user_id('lenka'))
    get_user_id('lenka')


    add_user_product('lenka')
    pass

>>>>>>> Stashed changes

if __name__ == '__main__':
    print("populating script!")
    runner()
