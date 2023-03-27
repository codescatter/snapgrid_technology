from django import contrib
from django.db.models.fields.related import ForeignKey
from django.shortcuts import redirect, render
from .form import CustomerRegistration,CustomerLogin,UserPasswordchange,Userchangeprofile
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Contact, Query, About, Php_intern, java_intern, django_intern, python_intern, ml_intern, ds_intern, ai_intern, android_intern
from django.core.mail import EmailMessage
# Create your views here.

def home(request):
    if request.method=="POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        website = request.POST["website"]
        message = request.POST["message"]
        
        messages.success(request, "Your query is registerd! HR will be contact get well soon....")
        obj = Query(name=name,email=email,phone=phone,website=website,message=message)
        obj.save()
        emailsent = EmailMessage('Query Registerd', 'HR contact get well soon',to=[email])
        emailsent.send()
        emailsent = EmailMessage(f'Tack a query for that user {name}', f'Query of {message}',to=["hgadhiya8980@gmail.com"])#,"lalitsolanki2610@gmail.com"])
        emailsent.send()
        return redirect("home")

    return render(request, 'index.html')

def contact(request):
    data = Contact.objects.all()
    if request.method=="POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        website = request.POST["website"]
        message = request.POST["message"]
        
        messages.success(request, "your query is registerd! HR will be contact get well soon....")
        
        obj = Contact(name=name,email=email,phone=phone,website=website,message=message)
        obj.save()
        emailsent = EmailMessage('Your contact Registerd', 'HR contact get well soon',to=[email])
        emailsent.send()
        emailsent = EmailMessage(f'Tack a contact for that user {name}', f'Query of {message}',to=["hgadhiya8980@gmail.com"])#,"lalitsolanki2610@gmail.com"])
        emailsent.send()
        return redirect("contact")
    
    content = {"data":data}
    return render(request, "contact.html", content)

def about(request):
    if request.method=="POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        website = request.POST["website"]
        message = request.POST["message"]
        messages.success(request, "your query is registerd! HR will be contact get well soon....")
        
        obj = About(name=name,email=email,phone=phone,website=website,message=message)
        obj.save()
        return redirect("about")
    return render(request, "about.html")

def login_form(request):
    form = CustomerLogin()
    if request.method == 'POST':
        uname = request.POST['username']
        upass = request.POST['password']
        user = authenticate(username=uname,password=upass)
        if user is None:
            messages.error(request,'Please Enter Correct Credinatial')
            return redirect('login_form')
        else:
            login(request,user)
            messages.success(request,'Login Successful')
            return redirect('home')
    else:
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return render(request,'login-form.html',{'form':form})
        
def Logout(request):
    logout(request)
    messages.info(request,'Logout Successful')
    return redirect("login_form")

def signup_form(request):
    if request.method == "POST":
        form = CustomerRegistration(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            print(username)
            form.save()
            messages.success(request,f'{username} Successfully Registred !!!')
            emailsent = EmailMessage('Registerd', 'Registerd Successfully!!!',to=[email])
            emailsent.send()
            emailsent = EmailMessage(f'Register for that user {username}', 'Registered successfully..',to=["hgadhiya8980@gmail.com"])#,"lalitsolanki2610@gmail.com"])
            emailsent.send()
            return redirect("login_form")
    else:
        form = CustomerRegistration()
    con = {'form':form}
    return render(request, 'signup-form.html',con)

def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UserPasswordchange(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Password Change successfully')
                return redirect('login_form')
        else:
            form = UserPasswordchange(user = request.user)
        return render(request, 'change-password.html', {'form':form})
    else:
        messages.info(request,'Please Login First')
        return redirect('login_form')


def update_profile(request):
    if request.user.is_authenticated:
        form = Userchangeprofile(instance=request.user)
        if request.method == "POST":
            form = Userchangeprofile(request.POST,instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request,"Profile Update Successfully")
                return redirect('update_profile')
            else:
                form = Userchangeprofile(instance=request.user)
        return render(request,'update_profile.html', {'form':form})
    else:
        messages.info(request,"you have first login")
        return redirect('login_form')
    
    
def app_dev(request):
    return render(request, "app-development.html")

def digital_marketing(request):
    return render(request, "digital-marketing.html")

def ecommerce(request):
    return render(request, "ecommerce.html")

def hosting(request):
    return render(request, "hosting.html")

def ml(request):
    return render(request, "machine-learning.html")

def my_account(request):
    return render(request, "my-account.html")

def seo(request):
    return render(request, "seo.html")

def support(request):
    return render(request, "support-maintance.html")

def ui(request):
    return render(request, "Ui-ux.html")

def web_design(request):
    return render(request, "web-design.html")

def web_development(request):
    return render(request, "web-development.html")

def php_intern(request):
    data = Php_intern.objects.all()
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        city = request.POST["city"]
        address = request.POST["address"]
        messages.success(request, "your query is registerd! HR will be contact get well soon....")
        
        obj = Php_intern(name=name,email=email,phone=phone,city=city,address=address)
        obj.save()
        emailsent = EmailMessage('Intership', 'You have succesfully register for php internship..',to=[email])
        emailsent.send()
        emailsent = EmailMessage(f'student {name} apply for php internship', f'user contact number is {phone}',to=["hgadhiya8980@gmail.com"])#,"lalitsolanki2610@gmail.com"])
        emailsent.send()
        
    return render(request, "php-intership.html",{"data":data})


def Django_intern(request):
    data = django_intern.objects.all()
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        city = request.POST["city"]
        address = request.POST["address"]
        messages.success(request, "your query is registerd! HR will be contact get well soon....")
        
        obj = django_intern(name=name,email=email,phone=phone,city=city,address=address)
        obj.save()
        emailsent = EmailMessage('Intership', 'You have succesfully register for python-django internship..',to=[email])
        emailsent.send()
        emailsent = EmailMessage(f'student {name} apply for django internship', f'user contact number is {phone}',to=["hgadhiya8980@gmail.com"])#,"lalitsolanki2610@gmail.com"])
        emailsent.send()
        
    return render(request, "django-intership.html",{"data":data})

def Java_intern(request):
    data = java_intern.objects.all()
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        city = request.POST["city"]
        address = request.POST["address"]
        messages.success(request, "your query is registerd! HR will be contact get well soon....")
        
        obj = java_intern(name=name,email=email,phone=phone,city=city,address=address)
        obj.save()
        emailsent = EmailMessage('Intership', 'You have succesfully register for java internship..',to=[email])
        emailsent.send()
        emailsent = EmailMessage(f'student {name} apply for java internship', f'user contact number is {phone}',to=["hgadhiya8980@gmail.com"])#,"lalitsolanki2610@gmail.com"])
        emailsent.send()
        
    return render(request, "java-intership.html",{"data":data})


def Android_intern(request):
    data = android_intern.objects.all()
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        city = request.POST["city"]
        address = request.POST["address"]
        messages.success(request, "your query is registerd! HR will be contact get well soon....")
        
        obj = android_intern(name=name,email=email,phone=phone,city=city,address=address)
        obj.save()
        emailsent = EmailMessage('Intership', 'You have succesfully register for android internship..',to=[email])
        emailsent.send()
        emailsent = EmailMessage(f'student {name} apply for android internship', f'user contact number is {phone}',to=["hgadhiya8980@gmail.com"])#,"lalitsolanki2610@gmail.com"])
        emailsent.send()
    return render(request, "android-intership.html",{"data":data})


def Python_intern(request):
    data = python_intern.objects.all()
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        city = request.POST["city"]
        address = request.POST["address"]
        messages.success(request, "your query is registerd! HR will be contact get well soon....")
        
        obj = python_intern(name=name,email=email,phone=phone,city=city,address=address)
        obj.save()
        emailsent = EmailMessage('Intership', 'You have succesfully register for python internship..',to=[email])
        emailsent.send()
        emailsent = EmailMessage(f'student {name} apply for python internship', f'user contact number is {phone}',to=["hgadhiya8980@gmail.com"])#,"lalitsolanki2610@gmail.com"])
        emailsent.send()
        
    return render(request, "python-intership.html",{"data":data})

def Ml_intern(request):
    data = ml_intern.objects.all()
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        city = request.POST["city"]
        address = request.POST["address"]
        messages.success(request, "your query is registerd! HR will be contact get well soon....")
        
        obj = ml_intern(name=name,email=email,phone=phone,city=city,address=address)
        obj.save()
        emailsent = EmailMessage('Intership', 'You have succesfully register for machine learning internship..',to=[email])
        emailsent.send()
        emailsent = EmailMessage(f'student {name} apply for machine learning internship', f'user contact number is {phone}',to=["hgadhiya8980@gmail.com"])#,"lalitsolanki2610@gmail.com"])
        emailsent.send()
        
    return render(request, "ml-internship.html",{"data":data})


def Ai_intern(request):
    data = ai_intern.objects.all()
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        city = request.POST["city"]
        address = request.POST["address"]
        messages.success(request, "your query is registerd! HR will be contact get well soon....")
        
        obj = ai_intern(name=name,email=email,phone=phone,city=city,address=address)
        obj.save()
        emailsent = EmailMessage('Intership', 'You have succesfully register for artificial inteligense internship..',to=[email])
        emailsent.send()
        emailsent = EmailMessage(f'student {name} apply for artificial inteligense internship', f'user contact number is {phone}',to=["hgadhiya8980@gmail.com"])#,"lalitsolanki2610@gmail.com"])
        emailsent.send()
        
    return render(request, "ai-intership.html",{"data":data})


def Ds_intern(request):
    data = ds_intern.objects.all()
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        city = request.POST["city"]
        address = request.POST["address"]
        messages.success(request, "your query is registerd! HR will be contact get well soon....")
        
        obj = ds_intern(name=name,email=email,phone=phone,city=city,address=address)
        obj.save()
        emailsent = EmailMessage('Intership', 'You have succesfully register for data science internship..',to=[email])
        emailsent.send()
        emailsent = EmailMessage(f'student {name} apply for data science internship', f'user contact number is {phone}',to=["hgadhiya8980@gmail.com"])#,"lalitsolanki2610@gmail.com"])
        emailsent.send()
        
    return render(request, "ds-intership.html",{"data":data})

def services(request):
    return render(request, "services.html")

def php_project(request):
    return render(request, "php_project.html")

def android_project(request):
    return render(request, "android_project.html")

def asp_net_project(request):
    return render(request, "asp_net.html")

def java_project(request):
    return render(request, "java_project.html")

def python_project(request):
    return render(request, "python_project.html")

def django_project(request):
    return render(request, "django_project.html")

def ml_project(request):
    return render(request, "ml_project.html")

def ai_project(request):
    return render(request, "ai_project.html")

