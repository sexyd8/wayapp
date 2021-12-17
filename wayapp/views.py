import uuid
import requests
import json


from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.contrib.auth import logout, authenticate, login 
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash 
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages 
from django.contrib.auth.decorators import login_required 


from . forms import *
from . models import *

# Create your views here.
def index(request):
    foreign = Product.objects.filter(foreign=True)
    local = Product.objects.filter(local=True)
    latest = Product.objects.filter(latest=True)
    

    context = { 
        'foreign':foreign,
        'local':local,
        'latest':latest,
    }
    return  render(request, 'index.html', context)

def categories(request):
    categories=Category.objects.all()

    context = {
        'categories':categories
    }
    return render(request, 'category.html', context)



def diamond(request):
    diamond=Product.objects.filter(diamond=True)
    user= Profile.objects.get(user__username=request.user.username)
    upgrade = Member.objects.exclude(title='Wood')
    downgrade = Member.objects.exclude(title='Diamond')

    context = {
         'diamond':diamond,
        'user':user ,
        'upgrade':upgrade,
        'downgrade':downgrade
    }

    return render(request, 'diamond.html', context)

def gold(request):
    gold=Product.objects.filter(gold=True)
    user= Profile.objects.get(user__username=request.user.username)
    upgrade = Member.objects.exclude(title='Wood')
    downgrade = Member.objects.exclude(title='Diamond')

    context = {
         'gold':gold,
        'user':user ,
        'upgrade':upgrade,
        'downgrade':downgrade
    }

    return render(request, 'gold.html', context)


def wood(request):
    wood=Product.objects.filter(wood=True)
    user= Profile.objects.get(user__username=request.user.username)
    upgrade = Member.objects.exclude(title='Wood')
    downgrade = Member.objects.exclude(title='Diamond')

    context = {
        'wood':wood,
         'user':user ,
        'upgrade':upgrade,
        'downgrade':downgrade
    }

    return render(request, 'wood.html', context)


def dashboard(request):
    user = User.objects.get(username= request.user.username)
    if user:
        login(request, user)
        if Profile.objects.filter(user__username=request.user.username, member='Diamond'):
            return redirect('diamond')
        elif  Profile.objects.filter(user__username=request.user.username, member='Gold'):
            return redirect('gold')
        else:
            return redirect('wood')
    else:
        messages.warning(request, 'You have to login to view the Dashboard')
        return redirect('loginform')


def products(request):
    product=Product.objects.all().order_by('-id')

    context={
        'product':product
    }
    return render(request, 'products.html', context)




def details(request,id):
    details=Product.objects.get(pk=id)

    context={
        'details':details

    }
    return render(request, 'details.html',context)


def loginform(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            if Profile.objects.filter(user__username=request.user.username, member='Diamond'):
                messages.success(request, 'You can now watch movies of your choice!')
                return redirect('diamond')
            elif  Profile.objects.filter(user__username=request.user.username, member='Gold'):
                    messages.success(request, 'You can now watch movies of your choice!')
                    return redirect('gold')
            else:
                    messages.success(request, 'You can now watch movies of your choice!')
                    return redirect('wood')

        else:
            messages.info(request, 'Username/password incorrect')
            return redirect('loginform')

    return render(request, 'loginform.html')


def signupform(request):
    reg = SignupForm()
    if request.method == 'POST':
        reg = SignupForm(request.POST)
        if reg.is_valid():
            newreg = reg.save() 
            new = Profile(user=newreg)
            new.first_name = newreg.first_name
            new.last_name = newreg.last_name
            new.save()
            login(request,newreg)
            messages.success(request, 'Successfully!')
            return redirect('index')
        else:
            messages.warning(request, reg.errors)
            return redirect('signupform')
            
    context ={
        'reg': reg
    }
    return render(request, 'signup.html', context)



def password(request):
    update = PasswordChangeForm(request.user)
    if request.method=='POST':
        update=PasswordChangeForm(request.user, request.POST)
        if update.is_valid():
            user=update.save()
            update_session_auth_hash(request,user)
            messages.success(request, 'Password Update Successful')
            return redirect('index')
        else:
            messages.error(request, update.errors)
            return redirect('password')

    context={
        'update':update
    }
    return render(request, 'password.html', context)

def logoutfunc(request): 
    logout(request)
    return redirect('loginform')




def  profile(request):
    user= Profile.objects.get(user__username=request.user.username)
    upgrade = Member.objects.exclude(title='Wood')
    downgrade = Member.objects.exclude(title='Diamond')


    context={
        'user':user ,
        'upgrade':upgrade,
        'downgrade':downgrade
    }
    return render(request, 'profile.html', context)


def profileupdate(request):
    user= Profile.objects.get(user__username=request.user.username)
    form = ProfileForm(instance = request.user.profile)
    if request.method=='POST':
     form = ProfileForm(request.POST,  instance=request.user.profile)
     if form.is_valid:
         form.save()
         messages.success(request, 'Profile update successful')
         return redirect('profile')
         
    context = {
        'form': form,
           'user':user 
    }

    return render(request, 'profileupdate.html', context)



def membership(request, id):
    newmem = Member.objects.get(pk=id)
    form = MemberForm()
    if request.method == 'POST':
        gender = request.POST['gender']
        address = request.POST['address']
        phone = request.POST['phone']
        newmem = request.POST['new']
        fee = request.POST['newfee']
        form = MemberForm(request.POST)
        if form.is_valid():
            user = form.save() 
            new = Profile(user=user)
            new.first_name = user.first_name
            new.last_name = user.last_name
            new.email = user.email
            new.gender = gender
            new.address = address  
            new.phone = phone
            new.member = newmem
            new.fee = fee
            new.save()
            login(request,user)
            messages.success(request, 'You are one step away from completing your membership. confirm Phone number')
            return redirect('confirmation')
        else:
            messages.warning(request, form.errors)
            return redirect('index')
            
    context ={
        'form': form,
        'newmem':newmem,
    }
    return render(request, 'member.html', context)



def confirmation(request):
    user=User.objects.get(username=request.user.username)
    

    context={
        'user':user ,
    }
    return render(request, 'confirmation.html', context)



def memberfee(request):
    if request.method=='POST':
        api_key='sk_test_0e8a6068679eadbbbd2a7ff3a68f60bcf767faba'
        curl= 'https://api.paystack.co/transaction/initialize'
        cburl='http://localhost:8000/profile/'
        user= User.objects.get(username=request.user.username)
        total= float(user.profile.fee) *100
        pay_code= str(uuid.uuid4())
        # addmember = request.POST['addmember']
             

       #collect data that you will send to paystack
        headers={'Authorization': f'Bearer {api_key}'}
        data={'reference':pay_code,'email':user.email,'amount':int(total),'callback_url':cburl,'order_number':user.id}

        #make a call to paystack
        try:
            r=requests.post(curl, headers=headers, json=data)
        except Exception:
            messages.error(request, 'Network busy, try again')
        else:
            transback= json.loads(r.text)
            print('RESULT', transback)
            rd_url= transback['data']['authorization_url']

            paid = Membership()
            # profile = Profile.objects.get(user__username=request.user.username)
            paid.user=user .username
            paid.memeber_no=user .id
            paid.first_name=user .first_name
            paid.last_name=user .last_name
            paid.fee=total /100
            paid.pay_code=pay_code 
            paid.membership=user.profile.member
            paid.phone=user.profile.phone 
            paid.save()

            return redirect(rd_url)
    return redirect('confirmation')






def upgrade(request, id):
    single = Member.objects.get(pk=id)
    user=User.objects.get(username=request.user.username)
  
    context={
        'user':user ,
        'single':single
    }
    return render(request, 'upgrade.html', context)



def memberupgrade(request):
    if request.method=='POST':
        api_key='sk_test_0e8a6068679eadbbbd2a7ff3a68f60bcf767faba'
        curl= 'https://api.paystack.co/transaction/initialize'
        cburl='http://localhost:8000/profile/'
        user= User.objects.get(username=request.user.username)
        total= float(request.POST['newfee']) *100
        upgrade = request.POST['mem']
        pay_code= str(uuid.uuid4())
             

       #collect data that you will send to paystack
        headers={'Authorization': f'Bearer {api_key}'}
        data={'reference':pay_code,'email':user.email,'amount':int(total),'callback_url':cburl,'order_number':user.id}

        #make a call to paystack
        try:
            r=requests.post(curl, headers=headers, json=data)
        except Exception:
            messages.error(request, 'Network busy, try again')
        else:
            transback= json.loads(r.text)
            rd_url= transback['data']['authorization_url']

            
            pro = Profile.objects.get(user__username= request.user.username)
            paid = Membership()
            paid.user=user.profile.user
            paid.first_name=pro.first_name
            paid.last_name=pro.last_name
            paid.fee=total  /100
            paid.pay_code=pay_code 
            paid.membership= upgrade
            paid.phone=user.profile.phone 
            paid.save()

            profile = Profile()
            profile.first_name = pro.first_name
            profile.last_name = pro.last_name
            profile.email = pro.email
            profile.gender = pro.gender
            profile.address = pro.address  
            profile.phone = pro.phone
            profile.member = upgrade
            profile.fee = total  /100
            profile.member = upgrade
            profile.save()
            messages.success(request, 'Your membership has been upgraded ')
            return redirect(rd_url)
    return redirect('profile')



def downgrade(request, id):
    single = Member.objects.get(pk=id)
    user=User.objects.get(username=request.user.username)
  
    context={
        'user':user ,
        'single':single
    }
    return render(request, 'downgrade.html', context)




def memberdowngrade(request):
    if request.method=='POST':
        api_key='sk_test_0e8a6068679eadbbbd2a7ff3a68f60bcf767faba'
        curl= 'https://api.paystack.co/transaction/initialize'
        cburl='http://localhost:8000/profile/'
        user= User.objects.get(username=request.user.username)
        total= float(request.POST['newfee']) *100
        upgrade = request.POST['mem']
        pay_code= str(uuid.uuid4())
             

       #collect data that you will send to paystack
        headers={'Authorization': f'Bearer {api_key}'}
        data={'reference':pay_code,'email':user.email,'amount':int(total),'callback_url':cburl,'order_number':user.id}

        #make a call to paystack
        try:
            r=requests.post(curl, headers=headers, json=data)
        except Exception:
            messages.error(request, 'Network busy, try again')
        else:
            transback= json.loads(r.text)
            rd_url= transback['data']['authorization_url']

            
            pro = Profile.objects.get(user__username= request.user.username)
            paid = Membership()
            paid.user=user.profile.user
            paid.first_name=pro.first_name
            paid.last_name=pro.last_name
            paid.fee=total  /100
            paid.pay_code=pay_code 
            paid.membership= upgrade
            paid.phone=user.profile.phone 
            paid.save()

            profile = Profile()
            profile.first_name = pro.first_name
            profile.last_name = pro.last_name
            profile.email = pro.email
            profile.gender = pro.gender
            profile.address = pro.address  
            profile.phone = pro.phone
            profile.member = upgrade
            profile.fee = total  /100
            profile.member = upgrade
            profile.save()
            messages.success(request, 'Your membership has been downgraded ')
            return redirect(rd_url)
    return redirect('profile')



