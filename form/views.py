from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.db import IntegrityError
from django.contrib.auth import authenticate
from .models import Form
from .forms import SponsorForm
from django.contrib.auth.decorators import user_passes_test


# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {"form": UserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    username=request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('create_form')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'User already exists'
                })
        return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'Password do not match'
                })
        
def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('create_form')
        
@user_passes_test(lambda u: u.is_superuser)
def forms(request):
    forms = Form.objects.all()
    
    return render(request, 'forms.html', {
        'forms': forms
    })
    

def form_detail(request, form_id):
    if request.method == 'GET':
        form = get_object_or_404(Form, pk=form_id)
        sponsorform = SponsorForm(instance=form)
        return render(request, 'form_detail.html', {
            'form': form,
            'sponsorform': sponsorform
        })
    else:
        try:
            form = get_object_or_404(Form, pk=form_id)
            sponsorform = SponsorForm(request.POST, instance=form)
            form.save()
            return redirect('forms')
        except ValueError:
            return render(request, 'form_detail-html', {
                'form': form,
                'sponsorform': sponsorform,
                'error': 'Error updating task'
            })

def create_form(request):
    if request.method == 'GET':
        return render(request, 'create_form.html', {
            'sponsorform': SponsorForm()
        })
    else:
        sponsorform = SponsorForm(request.POST, request.FILES)
        if sponsorform.is_valid():
            new_form = sponsorform.save(commit=False)
            new_form.user = request.user
            new_form.receipt = sponsorform.cleaned_data['receipt']
            new_form.save()
            return redirect('create_form')
        else:
            return render(request, 'create_form.html', {
                'sponsorform': sponsorform,
                'error': 'Please provide valid data'
            })


