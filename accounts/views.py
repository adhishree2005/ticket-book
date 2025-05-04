from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from .models import CustomUser


class LoginView(View):
    template_name = 'accounts/login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, 'Username and password are required.')
            return render(request, self.template_name)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials.')
            return render(request, self.template_name)


class RegisterView(View):
    template_name = 'accounts/register.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')

        if not username or not email or not password:
            messages.error(request, 'All fields are required.')
            return render(request, self.template_name)

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, self.template_name)

        user = CustomUser.objects.create(
            username=username,
            email=email,
            phone_number=phone_number
        )
        user.set_password(password)
        user.save()

        messages.success(request, 'Registration successful. Please login.')
        return redirect(reverse_lazy('login'))


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, 'You have been successfully logged out.')
        return redirect(reverse_lazy('login'))
