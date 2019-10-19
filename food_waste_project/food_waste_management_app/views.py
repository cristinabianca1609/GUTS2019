from django.shortcuts import render
from django.http import HttpResponse

#Here you import any models that we will need to use
#from food_waste_management_app.models import 

# Create your views here.
def index(request):
    return render(request, 'food_waste_management_app/index.html') #path from templates
