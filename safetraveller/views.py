# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import re
from random import randint

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404,HttpResponseRedirect, JsonResponse
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.views import generic

from django.db import IntegrityError
from django.contrib.auth.models import User
from django.utils import timezone
import json
from datetime import timedelta, datetime
from django.core import serializers
from django.contrib.auth.decorators import login_required

from django.core import serializers
from django.core.urlresolvers import reverse

from django.contrib.auth import get_user_model
User=get_user_model()

# Create your views here.
def user_login(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('main')
	if request.POST:
			
		data=request.POST
		username = data['name']
		password = data['password']
		user = auth.authenticate(username=username, password=password)
		
		if user is not None:
			if user.is_active:
				login(request,user)
				# print(request.user.mineno)
			
				return HttpResponseRedirect('main')

			else:
				state = "Your account is not active, please contact the site admin."
				return render(request,'login.html', { 'state':state })
			# # print(request.user.mineno)
			# # print(request.user.mines)
		else:
				state = "Your username and/or password were incorrect."
				return render(request,'login.html', {'state':state})
		
		
	else:
		return render(request, 'login.html')


def register(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('main')
	if request.method=='POST': 
		data=request.POST
		up=User()
		up.username=data['name']
		up.set_password(data['password'])
		
		if re.match(r"[^@]+@[^@]+\.[^@]+", data['email'])==None:
			state="Invalid Email Address"
			return render(request,'login.html',{'state':state})
		up.email=data['email']
		
		try:
			up.save()
		except IntegrityError:
			state="Duplicacy in Username"
			return render(request,'login.html',{'state':state})
		up.save()
		return HttpResponseRedirect('login')
	else:
		# return HttpResponseRedirect('/')
		return render(request, 'login.html')

def main(request):
	if request.user.is_authenticated():
		return render(request, 'MainPage.html')
	return redirect('login')	



@login_required	
def user_logout(request):
	logout(request)
	# return render(request,'login.html')
	return redirect('login')
