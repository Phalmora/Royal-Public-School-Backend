from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('student_dashboard')  # Or teacher_dashboard depending on role
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

# Create your views here.
