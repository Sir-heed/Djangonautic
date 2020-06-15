from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Login the user
            login(request, user)
            return redirect('articles:list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Login the user
            user = form.get_user()
            login(request, user)
            # Check if there is a next field to redirect the user
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                # No redirect to previous link
                return redirect('articles:list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    # Changed form post to get
    # if request.method == 'POST':
    if request.method == 'GET':
        logout(request)
        return redirect('articles:list')
