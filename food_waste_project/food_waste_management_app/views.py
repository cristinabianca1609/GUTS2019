import datetime
from django.http import JsonResponse

import cv2

from django.shortcuts import render, render_to_response
from food_waste_management_app.forms import UserForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from ics import Calendar, Event

from food_waste_management_app.scanner import barcodeReader
from .models import User, UserProduct, Barcode


# Here you import any models that we will need to use
# from food_waste_management_app.models import

# Create your views here.
def index(request):
    return render(request, 'food_waste_management_app/index.html')  # path from templates


@login_required
def special(request):
    return HttpResponse("You are logged in!")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('food_waste_management_app:index'))


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True

        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request, 'food_waste_management_app/registration.html',
                  {'user_form': user_form,
                   'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('food_waste_management_app:index'))

            else:
                return HttpResponse('ACCOUNT NOT ACTIVE')

        else:
            print('Someone tried to login and failed.')
            return HttpResponse('invalid login details supplied!')
    else:
        return render(request, 'food_waste_management_app/login.html')

def food_monitor(request):
    return render(request, 'food_waste_management_app/food-monitor.html')

# def sample_view(request):
#     current_user = request.user
#     print current_user.id


#### Database Queries

def list_user_products(request):
    product_exp = dict()
    if request.method == 'GET':

        if request.user.is_authenticated:
            # username = request.user.username
            user_id = User.objects.filter(username=request.user.username)[0].id

            result = UserProduct.objects.all().filter(user_id=user_id)
            for i in result:
                name = Barcode.objects.filter(barcode_id=i.barcode_id)  # .values('product_name')
                # id : [product_name, exp_date]
                product_exp[i.user_product_id] = [name[0].product_name.strip('\n'), i.exp_date]
            print (product_exp)




        # data = Students.objects.all()

        stu = {
            "student_number": data
        }

        return render_to_response("food-monitor.html", product_exp)



        return JsonResponse(product_exp)  # dictinary - list value
    return HttpResponse('this was called - cant believe')


# return JsonResponse({'foo':'bar'})


def scan_barcode():
    cap = cv2.VideoCapture(0)
    while (True):
        ret, frame = cap.read()
        barcode = barcodeReader(frame)
        if barcode is not None:
            print(barcode)
            return barcode
        # if code == ord('q'):
        #     break

def add_user_product(request):
    product_dict = dict()
    if request.user.is_authenticated:
        username = request.user.username
        # user_id = User.objects.filter(username=request.user.username)[0].id

        barcode_info = scan_barcode()
        # barcode_info = {'barcode': '123123', 'type': 'EAN13'}
        barcode = barcode_info['barcode']

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

    # return result
    return HttpResponse('this was called TOO - cant believe')
#
# def new_barcode(new_bar_dict):
#     new_bar = Barcode()
#     new_bar.barcode_no = new_bar_dict['barcode']
#     new_bar.product_name = new_bar_dict['name']
#     new_bar.save()

####video

def capture(request):
    return render(request, 'food_waste_management_app/capture.html')

@login_required
def download_ics(request):
    c = Calendar()
    e = Event()
    e.name = "Test Event"
    e.begin = "2020-01-01 00:00:00"
    c.events.add(e)

    return HttpResponse(content_type='application/force-download', content=c)

