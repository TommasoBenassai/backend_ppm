from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.views.generic import TemplateView
from django import forms
from django.contrib.auth.models import User



def user_signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']

            try:
                # Verifica se l'email è già presente nel sistema
                User.objects.get(email=email)
                form.add_error('email', 'Questa email è già stata registrata.')
            except User.DoesNotExist:
                # Crea un nuovo oggetto User
                user = User.objects.create_user(username=username, password=password, email=email)

                login(request, user)
                return redirect(reverse('product_list'))
    else:
        form = CustomUserCreationForm()
    return render(request, 'authentication/signup.html', {'form': form})


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('product_list'))
        else:
            return render(request, 'authentication/login.html', {'error': 'Credenziali non valide.'})
    else:
        return render(request, 'authentication/login.html')



def user_logout(request):
    logout(request)
    return redirect('homepage')



