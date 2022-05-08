from bugs.models import Bug,BugType
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from core.forms import  JoinForm, LoginForm
# Create your views here.
