import datetime
import csv
import re

import razorpay
import stripe
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse
from validate_email import validate_email
import requests
import qrcode
from .models import datetime1,contactus,register,products,BioData
from django.shortcuts import render, redirect
from django.http import HttpResponse,FileResponse
from django.contrib.auth.models import auth,User
from django.contrib.auth.decorators import login_required
from django.conf import settings
def index(request):
    return render(request,'navbar.html')

def home(request):
    print(request.session.get('user_email'))
    print(request.session.session_key)
    return render(request, "home.html",{"name":f"Agriculture Busiess System"})


def mydata(request):
    return HttpResponse('Name: pranith<br>Id: 2100031054 ')

def date(request):
    var1=datetime.datetime.now()
    data=datetime1(time1=var1)
    data.save()
    return HttpResponse(var1)

def rendertemp(request):
    return render(request,'temperature.html')

def temperature(request):
    if request.method=='POST':
        place = request.POST.get('temp')

        api_key = 'fbdcb3297c21556bdbaf6445e3d56559'

        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={place}&units=imperial&APPID={api_key}")

        if weather_data.json()['cod'] == '404':
            return HttpResponse('error')
        else:
            weather = weather_data.json()['weather'][0]['main']
            temp = round(weather_data.json()['main']['temp'])
            # °C = [(°F-32)×5] / 9
            temp1 = (((temp - 32) * 5) / 9)
            # print(type(temp))
            print(f"The weather in {place} is: {weather}")
            print(f"The temperature in {place} is: {temp}ºF")
            print(f"The temperature in {place} is: {temp1}ºC")
        return HttpResponse(
            f'the weather in {place} is {weather}\nThe temperature in {place} is: {temp}ºF\nThe temperature in {place} is: {temp1}ºC')
    return HttpResponse("Error")

def renderqr(request):
    return render(request,'qrcode1.html')


def qrcode1(request):
    if request.method=='POST':

        sid=request.POST.get('sid')
        sname=request.POST.get('sname')
        data=sid+sname

        qr=qrcode.QRCode(version=1,box_size=25,border=5)
        qr.add_data(data)

        qr.make(fit=True)
        img=qr.make_image(fill_color='black',back_color='white')

        img.save('static/images/KLU.png')
        img1=open('static/images/KLU.png','rb')
        return FileResponse(img1)
    else:
        return HttpResponse("Not Working")

@login_required(login_url="/renderlogin")
def rendercontact(request):
    return render(request,'contact.html')

def contactus1(request):
    if request.method=='POST':

        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        comment=request.POST['comment']
        # tosend=comment+"\n------------------------Thank You------------------------"
        data=contactus(firstname=firstname,lastname=lastname,email=email,comment=comment)
        data.save()
        # send_mail("Thank you for contacting us",tosend,'saikotti2@gmail.com',[email],fail_silently=False)
        return HttpResponse('Sent')
    else:
        return HttpResponse("ERROR")
    # if request.method=='POST':
    #     tosend = "repu collage ki holiday"
    #
    #     with open(r"D:\pfsd\Django_projects\AAS\static\try.csv", 'r') as f:
    #         reader = csv.reader(f)
    #         next(reader)
    #         for email in reader:
    #             send_mail("Thank you for contacting us", tosend, 'saikotti2@gmail.com', [email[1:len(email)]], fail_silently=False)
    #     return HttpResponse("mails sent")

def renderlogin(request):
    return render(request,'login.html')


def login(request):

    if request.method=='POST':
        data=register.objects.all()

        username=request.POST['uname']
        pwd=request.POST['pass']
        obj=None
        for i in data:
            if i.username==username:
                obj=i

        user=auth.authenticate(username=username,password=pwd)
        if user is not None:
            request.session['user_id']=user.id
            request.session['user_email']=user.email

            auth.login(request,user)
            if obj.is_admin:
                response=HttpResponse(render(request,'adminhome.html '))
                response.set_cookie('mycookie',request.session.session_key)
                return response
            return  redirect('/')

        else:
            return render(request,'error.html',{"error":"Enter valid credentials"})
    else:
        return HttpResponse("Try Again")

def renderregister(request):
    return render(request,'register.html')

def registeruser(request):
    if request.method=='POST':
        pattern = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        username=request.POST['uname']
        email=request.POST['mail']
        mobile=request.POST['mobile']
        pwd=request.POST['pass']
        cpwd=request.POST['cpass']
        # role=request.POST['role']
        if pwd!=cpwd:
            messages.error(request,'check the password and try again')
            return redirect('/renderregister')
        if len(mobile)!=10 or mobile.startswith('0'):
            messages.error(request,'enter a valid phone number')
            return redirect('/renderregister')
        if len(username)<8 or username.isalnum()==False:
            messages.error(request,'Enter valid username')
            return redirect('/renderregister')
        if re.search(pattern,email) is None:
            messages.error(request,'enter a valid email')
            return redirect('/renderregister')
        if len(pwd)<8:
            messages.error(request,'Password should have more than 8 characters')
            return redirect('/renderregister')
        is_admin=False
        # if role=='admin':
        #     is_admin=True
        # if role=="user":
        #     is_admin=False
        # data=register(username=username,email=email,mobile=mobile,password=pwd)
        # data.save()
        # return HttpResponse("<center><h1>User Sucessfully Registered</h1></center>")
        user=User.objects.create_user(username=username,email=email,password=pwd)
        user.save()
        data=register(username=username,mobile=mobile,email=email,password=pwd)
        data.save()
        return redirect('/')

@login_required(login_url="/renderlogin")
def renderbuy(request):
    data=products.objects.all()

    return render(request,'buy.html',{'data':data})

stripe.api_key=settings.STRIPE_SECERET_KEY
def buy(request):
    if request.method == 'POST':
        item=request.POST['item']
        print(item)
        prods=products.objects.all()
        obj=None
        for i in prods:
            if item==i.item:
                obj=i
                break
        return render(request,'checkout.html',{'data':obj})


    return HttpResponse("hello")

@login_required(login_url="/renderlogin")
def about(request):

    return render(request,'about.html')

def renderfeedback(request):
    return render(request,'feedback.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def adminhome(request):
    return render(request,'adminhome.html')

def users(request):
    data=register.objects.all()
    return render(request,'users.html',{"data":data})

def contactreviews(request):
    data=contactus.objects.all()
    return render(request,'contactdetails.html',{"data":data})

def forgetpassword(request):
    if request.method=='POST':
        username=request.POST['username']
        data = register.objects.all()
        for i in data:
            if i.username==username:
                email=i.email
                tosend=i.password
                send_mail("you got your password back", tosend, 'saikotti2@gmail.com', [email], fail_silently=False)
                return HttpResponse("password sent to your mail"
                                    "")
        else:
            return HttpResponse("You dont have an account ")
        return HttpResponse(username)

    return render(request,'forgetpassword.html')

def items(request):
    product =products.objects.all()
    data = {
        'products': product
    }

    for i in product:
        print(i.photo.url)
    return render(request,'items.html',data)

def additem(request):
    if request.method=='POST' and request.FILES['photo']:

        item = request.POST['item']
        cost = request.POST['cost']
        photo = request.FILES['photo']
        products.objects.create(item=item,cost=cost,photo=photo)
        return redirect('items')
    return render(request, 'additem.html')

def biodata(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname = request.POST['lastname']
        dob = request.POST['dob']
        phone = request.POST['phone']
        data=BioData(firstname=firstname,lastname=lastname,dob=dob,phone=phone)
        data.save()
        return HttpResponse("Data saved in database")
    return render(request,'biodata.html')

def checkout(request):
    if request.method=='POST':
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=[
                'card',
            ],
            line_items=[
                {
                    'price': 'price_1N4wc2SC8a6sTaYDwADOnywV',
                    'quantity': 1,
                }
            ],
            mode='payment',
            success_url='http://127.0.0.1:8000/',
            cancel_url='http://127.0.0.1:8000/',
        )
        return redirect(checkout_session.url,code=303)
    return HttpResponse('error')
