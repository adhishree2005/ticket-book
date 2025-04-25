from django.views.generic import FormView, View, CreateView  # Added CreateView here
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django import forms
from django.contrib import messages
from .models import CustomUser
from django.shortcuts import redirect

# Custom Login Form
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

# Login View
class LoginView(FormView):
    template_name = 'accounts/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home')  # Adjust the success URL to where you want to redirect after login.

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        
        if user is not None:
            login(self.request, user)  # Log the user in
            return super().form_valid(form)  # Redirect to success URL
        else:
            messages.error(self.request, 'Invalid username or password')
            return self.form_invalid(form)  # Return to the form with an error message

# Register View
class RegisterView(CreateView):
    model = CustomUser
    template_name = 'accounts/register.html'
    fields = ['username', 'email', 'password', 'phone_number']
    success_url = reverse_lazy('login')  # Redirect to login after successful registration

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])  # Ensure password is hashed
        user.save()
        messages.success(self.request, 'Registration successful. Please login.')
        return super().form_valid(form)

# Logout View
class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)  # Logs the user out
        messages.success(request, 'You have been successfully logged out.')
        return redirect(reverse_lazy('login'))  # Redirect to login page after logout
