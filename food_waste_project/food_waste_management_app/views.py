from django.shortcuts import render
from food_waste_management_app.forms import UserForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from ics import Calendar, Event
from food_waste_management_app.models import UserProduct


#Here you import any models that we will need to use
#from food_waste_management_app.models import

# Create your views here.
def index(request):
    return render(request, 'food_waste_management_app/index.html') #path from templates

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

        user = authenticate(username = username, password = password)

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

@login_required
def download_ics(request):
    c = Calendar()
    e = Event()
    e.name = "Test Event"
    e.begin = "2020-01-01 00:00:00"
    c.events.add(e)

    #return HttpResponse(content_type='application/force-download', content=c)
    return HttpResponse(UserProduct.objects.all())
