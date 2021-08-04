from myapp.models import Comment
import random
import string
import re
from django.http import HttpResponse
from .forms import MyForm, AuthenticationForm, UserRegistrationForm, Password_change, Get_Comment
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

def start_page(request):
    return render(request,'start_page.html')

def articles(request):
    return render(request, 'articles.html')

def archive_article(request):
    return render(request, 'archive_article.html')

def users(request):
    return render(request, 'users.html')

def article_num(request, article_number):
    context = {
        "article_number": article_number,
    }
    return render(request, 'check.html', context)

def article_num_archive(request, user_number):
    return HttpResponse(
        "This is an user #{}".format(user_number))

def article_num_slug(request, article_number, slug_text):
    context = {
        "article_number": article_number,
        "slug": slug_text,
    }
    return render(request, 'slug.html', context)

def users_num(request, user_number):
    return HttpResponse(
        "This is an user #{}".format(user_number))

def verification_number(request, phone):
    return HttpResponse(
         "This is users phone number: #{}. {}".format(phone, "{}".format(
            "Valid phone number") if re.search("^\+?3?8?(0\d{9})$", phone) else "Invalid phone number"))

def symbols(request, symb=''):
    return HttpResponse(
         "This is symbols: #{}. {}".format(symb, "{}".format(
            "Valid symbols") if re.search('^[1-9a-f]{4}-[a-zA-Z0-9]{6}\b', symb) else "Invalid symbols"))

def form_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
           return render(request, 'form_was_valid.html')

    else:
        form = MyForm()

    return render(request, 'form.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            login(request, form.user)
            return HttpResponse('Authenticated successfully')
        else:
            return HttpResponse('Invalid login')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return render(request, 'success_registration.html', {'new_user': new_user})
        
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration.html', {'user_form': user_form})

@login_required(login_url='/login/')
def change_password(request):
    if request.method == 'POST':
        form = Password_change(request.POST)

        if form.is_valid():
            username = request.user.username
            password = form.cleaned_data['password']
            new_password = form.cleaned_data['new_password']
            user = User.objects.get(username=username)
            if user.check_password(raw_password=password):
                user.set_password(raw_password=new_password)
                user.save()
                messages.success(request, 'Password succesfully changed')
                return redirect('change_password')
        else:
            messages.error(request, 'Correct the error')
    else:
        form = Password_change()
    return render(request, 'change_password.html', {'form': form})   

@login_required(login_url='/login')
def get_comment(request):
    if request.method == "GET":
        form = Get_Comment(request.GET)
        if form.is_valid():
            user_request = form.cleaned_data.get("search")
            if user_request is not None:
                result = Comment.objects.filter(text__icontains=user_request).values_list('text', flat=True)
            else:
                result = Comment.objects.values('text')
    return render(request, 'get_comment.html', {'form': form, 'result': result})
    