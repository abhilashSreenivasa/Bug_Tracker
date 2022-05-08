from core.models import UserProfile,Role
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from core.forms import  JoinForm, LoginForm

# Create your views here.

def home(request):
    return render(request,"test.html",{})

def join(request):
    if (request.method == "POST"):
        join_form = JoinForm(request.POST)
        if (join_form.is_valid()):

            # Save form data to DB
            user=UserProfile()
            user.username=join_form.cleaned_data['username']
            user.email=join_form.cleaned_data['email']
            user.set_password(join_form.cleaned_data['password'])
            role_id=''+join_form.cleaned_data['role']
            print(role_id)
            user.role=Role.objects.get(role_id=role_id)
            # Save encrypted password to DB
            user.save()
            # Success! Redirect to home page.
            return redirect("/admin")
        else:
            page_data = { "join_form": join_form }
            return render(request, 'join.html', page_data)

    else:
        join_form = JoinForm()
        page_data = { "join_form": join_form }
        return render(request, 'join.html',page_data)
