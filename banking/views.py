from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import UserAccount, BankDetails
import random
# Create your views here.

def signup(request):
    banks = BankDetails.objects.values('bank_name').distinct()
    data = {
        'banks':banks
    }
    account_no = int(''.join(str(random.randint(0,9)) for _ in range(11)))
    if request.POST:
        fname       = request.POST.get('fname',False)
        lname       = request.POST.get('lname',False)
        username    = request.POST.get('username',False)
        email       = request.POST['email']
        password    = request.POST['password']
        user = User.objects.create_user(username, email, password, first_name=fname, last_name=lname)
        user.save()
        phone       = request.POST.get('phone')
        dob         = request.POST.get('dob')
        address     = request.POST.get('address')
        bank        = request.POST.get('bank')
        UserAccount.objects.create(user_id=user.id,phone=phone,dob=dob,address=address,bank=bank)
        return redirect(home)
    return render(request,'signup.html',data)

def getbranches(request):
    branches = list(BankDetails.objects.filter(bank_name=request.GET['bank']).values())
    return JsonResponse(branches, safe=False)

def home(request):
    if request.POST:
        username       = request.POST.get('username',False)
        password       = request.POST.get('password',False)
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect(dashboard)
        else:
            pass
            # No backend authenticated the credentials
    return render(request,'login.html',{})

def dashboard(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect(home)
    return render(request,'index.html',{})

def transactions(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect(home)
    return render(request,'transactions.html',{})

def user_logout(request):
    logout(request)
    return redirect(home)

def transaction(request):
    return render(request,'login.html',{})