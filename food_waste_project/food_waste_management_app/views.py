from django.shortcuts import render
from django.http import HttpResponse
from food_waste_management_app.forms import UserForm

#Here you import any models that we will need to use
#from food_waste_management_app.models import

# Create your views here.
def index(request):
    return render(request, 'food_waste_management_app/index.html') #path from templates


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
