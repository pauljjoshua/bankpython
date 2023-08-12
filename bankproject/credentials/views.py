from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.forms import ModelForm
from .models import details


# Create your views here.
def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('app')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
        return redirect('form.html')
    return render(request,'login.html')

def register(request):

    if request.method=='POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'user name taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)

                user.save();
                return redirect('login')

        else:
            messages.info(request,'password not matched')
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

# def form(request):
#     messages.info(request, 'Application Accepted')
#     return render(request,'form.html')

def form(request):
    if request.method == 'POST':
        name = request.POST.get('name', )
        dob = request.POST.get('dob', )
        age = request.POST.get('age', )
        gender = request.POST.get('gender', )
        mob_no = request.POST.get('mob', )
        email = request.POST.get('email', )
        address = request.POST.get('address', )

        detail = details(name=name, date_of_birth=dob, gender=gender, mob_no=mob_no, age=age, email=email,
                         address=address)
        detail.save()
        return render(request, 'DROPDOWN.html')
    return render(request, 'form.html')


def DROPDOWN(request):
    return render(request,'DROPDOWN.html')


def app(request):
    return render(request,'app.html')

def fo(request):
    return render(request,'fo.html')

# def form(request):
#     if request.method == 'POST':
#         name = request.POST.get('name', )
#         dob = request.POST.get('dob', )
#         age = request.POST.get('age', )
#         gender = request.POST.get('gender', )
#         mob_no = request.POST.get('mob', )
#         email = request.POST.get('email', )
#         address = request.POST.get('address', )
#
#
#         try:
#             user = User.objects.get(username=name)
#             user1 = User.objects.get(age=age)
#             user2 = User.objects.get(dob=dob)
#             user3 = User.objects.get(gender=gender)
#             user4 = User.objects.get(mob=mob_no)
#             user5 = User.objects.get(email=email)
#             user5 = User.objects.get(address=address)
#
#         except User.DoesNotExist:
#             messages.info(request, 'invalid')
#             return render(request, 'form.html', {'error': 'Invalid username'})
#
#
#
#         request.user = user
#         return redirect('DROPDOWN')
#         request.user = user
#         return redirect('DROPDOWN')
#         request.user = user
#         return redirect('DROPDOWN')
#         request.user = user
#         return redirect('DROPDOWN')
#
#     else:
#         return render(request, 'form.html')


# def form(request):
#     form = detailsForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return render(request, 'DROPDOWN.html')
#     return render(request, 'form.html', {'form': form})

