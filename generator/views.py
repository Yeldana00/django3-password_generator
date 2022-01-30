import random
import re
from django.shortcuts import render
from django.http import HttpResponse
	
    
def home(request):
	return render(request, 'generator/home.html')

def password(request):
	characters = list('qwertyuiopasdfghjklzxcvnm')
	if request.GET.get('uppercase'):
		characters.extend(list('QWERTYUIOPASDFFGHJKLZXCVBNM'))
	if request.GET.get('special'):
		characters.extend(list('!@#$%^&*_()'))
	if request.GET.get('numbers'):
		characters.extend(list('1234567890'))

	length = int(request.GET.get('length',12))

	thepassword = ''
	for i in range(length):
		thepassword += random.choice(characters)
	return render(request,'generator/password.html',{'password': thepassword})

def about(request):
	return render(request,'generator/about.html')