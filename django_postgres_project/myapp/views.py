from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature

def index(request):
    # feature1 = Feature()
    # feature1.id = 0
    # feature1.name = "Fast"
    # feature1.detail = "This is very fast!"
    # feature1.is_true = True

    # feature2 = Feature()
    # feature2.id = 1
    # feature2.name = "Loud"
    # feature2.detail = "This is very Loud!"
    # feature2.is_true = False

    # feature3 = Feature()
    # feature3.id = 2
    # feature3.name = "Looks"
    # feature3.detail = "This looks really great!"
    # feature3.is_true = True

    # features = [feature1, feature2, feature3]

    features = Feature.objects.all()

    return render(request, 'index.html', {'features':features})


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already in use')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'Passwords are not the same')
            return redirect('register')
    
    else:
        return render(request, 'register.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')

def post(request, pk):
    return render(request, 'post.html', {'pk':pk})

# def counter(request):
#     text = request.POST['text']
#     amount_of_words = len(text.split())
#     return render(request, 'counter.html', {'amount':amount_of_words})

def counter(request):
    blogs = [1,2,3,4,5,"tim", "tom", "john"]
    return render(request, 'counter.html', {'blogs':blogs})