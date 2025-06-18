from django.shortcuts import render
from django.http import HttpResponse
from .models import Registration,Skilled_Jobs,Unskilled_Jobs

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
 
def register(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        number = request.POST.get('mobile_number', '').strip()
        email = request.POST.get('email', '').strip()
        qualification = request.POST.get('Qualification', '').strip()
        where = request.POST.get('where', '').strip()

        errors = []

        # Basic validation
        if not name:
            errors.append("Name is required.")
        
        if not number:
            errors.append("Mobile number is required.")
        elif not re.match(r'^\d{10}$', number):
            errors.append("Mobile number must be 10 digits.")

        if not email:
            errors.append("Email is required.")
        else:
            try:
                validate_email(email)
            except ValidationError:
                errors.append("Enter a valid email address.")
        
        if not qualification:
            errors.append("Qualification is required.")
        
        if not where:
            errors.append("Origin (where are you from) is required.")

        # If errors, return the same page with error messages
        if errors:
            return render(request, 'index.html', {'errors': errors})

        # Save to DB if all data is valid
        new_Registration = Registration(
            name=name,
            mobile_number=number,
            email=email,
            Qualification=qualification,
            where_are_you_from=where
        )
        new_Registration.save()
        return render(request, 'index.html', {'success': "Registration successful! Our Executive will get in touch with you soon"})

    return render(request, 'index.html')
