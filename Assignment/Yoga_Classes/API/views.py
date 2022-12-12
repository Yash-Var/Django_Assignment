from django.shortcuts import render, redirect
from .models import User
from django.http import HttpResponse

# Create your views here.

def ValidateAndSaveData(request):
    
    if request.method == 'POST':
        
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']

        if name == "" or age == "" or email == "":
            return HttpResponse('Please fill all details')

        if int(age) < 18 or int(age) > 65:
            return HttpResponse('Error! Age must be between 18 and 65')

        if not User.objects.filter(email = email).exists():
            newUser = User(name = name, email = email, age = age)
            newUser.save()
            return HttpResponse('Details have been successfully submitted!')
        else:
            return HttpResponse('Email already exists!')

    return render(request, 'index.html', {})

def CompletePayment(user):
    # currentUser = User.objects.filter(email = user.email)

    # currentUser['paymentStatus'] = true
    # return HttpResponse('Payment done!')
    pass