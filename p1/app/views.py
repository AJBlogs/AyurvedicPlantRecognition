from django.shortcuts import render, redirect
#from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm,SignUpForm
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


#--------------------                           Main Page                      -----------------------------------
def index(request):
    return render(request, 'index.html')


from .models import ContactMessage

def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save to database
        contact_message = ContactMessage(name=name, email=email, message=message)
        contact_message.save()

        # Send email
        """ subject = f'Contact Form Submission from {name}'
        body = f'Name: {name}\nEmail: {email}\nMessage: {message}'
        send_mail(
            subject,
            body,
            email,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        ) """

        return render(request, 'contact_us.html', {'form': ContactMessage(), 'success': True})
    

    return render(request, 'contact_us.html')





#--------------------                           SignUP                     -----------------------------------
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

#--------------------                           Login Page                    -----------------------------------
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})