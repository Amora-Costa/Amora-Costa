from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Registration,Skilled_Jobs,Unskilled_Jobs,FAQ

# Create your views here.

from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.shortcuts import render
import re

def Home(request):
    skilled = Skilled_Jobs.objects.all()
    unskilled = Unskilled_Jobs.objects.all()
    return render(request,'index.html',
                  {'skilleds': skilled,
                   'unskilleds': unskilled })
 
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages
import re

def register(request):
    skilled = Skilled_Jobs.objects.all()
    unskilled = Unskilled_Jobs.objects.all()
    
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        number = request.POST.get('mobile_number', '').strip()
        email = request.POST.get('email', '').strip()
        qualification = request.POST.get('Qualification', '').strip()
        where = request.POST.get('where', '').strip()
        type = request.POST.get('typeofjob','').strip()

    
    
        if Registration.objects.filter(name=name).exists():
            messages.info(request,f"{name} already exist")

     

        if Registration.objects.filter(email=email).exists():
           messages.info(request,f"{email} already exist")
            
            
        # Basic validation
        if not name:
            messages.info(request, "Name is required.")
        elif not re.match(r'^[A-Za-z ]+$', name):
            messages.info(request,'Please enter a valid name.')
        
        if not number:
            messages.info(request, "Mobile number is required.")
        elif not re.match(r'^\d{10}$', number):
            messages.info(request, "Mobile number must be 10 digits.")

        if not email:
            messages.info(request, "Email is required.")
        else:
            try:
                validate_email(email)
            except ValidationError:
                messages.info(request, "Enter a valid email address.")
        
        if not qualification:
            messages.info(request, "Qualification is required.")
        
        if not where:
            messages.info(request, "Origin (where are you from) is required.")
        if not type:
            messages.info(request,'Please Select a job type')
        # ✅ Only save if no validation errors
        if not list(messages.get_messages(request)):
            new_Registration = Registration(
                name=name,
                mobile_number=number,
                email=email,
                Qualification=qualification,
                where_are_you_from=where,
                what_type_of_job = type
            )
            new_Registration.save()
            messages.info(request, "Registration successful! Our Executive will get in touch with you soon")

    return render(request, 'index.html', {
        'skilleds': skilled,
        'unskilleds': unskilled
    })


    return render(request, 'index.html' ,
                  {'skilleds': skilled,
                   'unskilleds': unskilled })



def faq_submit(request):
    if request.method == 'POST':
        question = request.POST.get('question', '').strip()
        if question:
            new_FAQ = FAQ(question=question)
            new_FAQ.save()
            messages.info(request, 'Question submitted successfully.')
        else:
            messages.info(request, 'Please enter a question.')
    
    return redirect('/')

        
        
   
 