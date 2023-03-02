import requests
from django.shortcuts import render, redirect
import random
from django.contrib import messages
import razorpay
# Create your views here.


from accounts.forms import personclass, personlogin
from accounts.models import User_accounts

def home(request):
    return render(request,'home.html')


def signup(request):
    form = personclass()
    return render(request, 'signup.html', {'form': form})


def saveuser(request):
    if request.method == 'POST':
        form = personclass(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'index.html')
        else:
            return render(request, 'signup.html', {'form': form})


def logpage(request):
    logform = personlogin(request.POST)
    return render(request, 'index.html', {'logform': logform})


def login(request):
    if request.method == 'POST':
        form = personlogin(request.POST)
        if form.is_valid():
            global mobile
            mobile = form.cleaned_data['phone_number']
            if User_accounts.objects.filter(phone_number=mobile).exists():
                obj = User_accounts.objects.filter(phone_number=mobile)
                # Generate a 4-digit random number
                global random_number
                random_number = random.randint(1000, 9999)
                # Print the generated number
                print(random_number)
                print(obj)
                print(mobile)

                url = "https://2factor.in/API/V1/603257ec-b14c-11ed-813b-0200cd936042/SMS/{mobile}/{random_number}/OTP1"
                params = { 'mobile': mobile,
                          'random_number': random_number}
                url = url.format_map(params)
                payload = {}
                headers = {}

                response = requests.request("GET", url, headers=headers, data=payload)

                print(response.text)

                return render(request, 'otp.html')

    logform = personlogin(request.POST)
    return render(request, 'index.html', {'logform': logform})


def resendotp(request):
    global random_number
    random_number = random.randint(1000, 9999)
    url = "https://2factor.in/API/V1/603257ec-b14c-11ed-813b-0200cd936042/SMS/{mobile}/{random_number}/OTP1"
    params = {'mobile': mobile,
              'random_number': random_number}
    url = url.format_map(params)
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)


    print(random_number)
    return render(request, 'otp.html')


def football(request):
    return render(request, 'football.html')


def otp(request):
    if request.method == 'POST':
        global random_number
        try:
            a = int(request.POST.get('first'))
            b = int(request.POST.get('second'))
            c = int(request.POST.get('third'))
            d = int(request.POST.get('fourth'))
            otp = int(str(a) + str(b) + str(c) + str(d))
            print(otp)
            print(type(otp))
            print(type(random_number))
            print(random_number)
            if otp == random_number:
                print("login succed")
                return redirect('football')

            else:
                messages.error(request, "plz enter a valid otp")
                return render(request, 'otp.html')
        except:
            messages.error(request, "plz enter a valid otp")
            return render(request, 'otp.html')




