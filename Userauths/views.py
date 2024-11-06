from django.shortcuts import render, redirect
from Userauths.forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Save the user to the database
            new_user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')  # Get the password from form data

            messages.success(request, f"Hey {username}, your account has been created successfully.")
            
            # Authenticate and log in the user
            new_user = authenticate(username=username, password=password)
            if new_user is not None:
                login(request, new_user)
                return redirect('home')  # Redirect to home or dashboard
            else:
                messages.error(request, 'Authentication failed.')
                return redirect('Userauths:signin')
        else:
            messages.error(request, 'There was an error with the submission.')
    else:
        form = RegisterForm()
    
    context = {
        'form': form
    }
    return render(request, 'Userauths/signup.html', context)


from Userauths.models import User

def login_view(request):
    if request.user.is_authenticated:
        return redirect('App:home')  # Redirect to home or dashboard if already authenticated
    
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.warning(request, f"User with email {email} does not exist.")
            return redirect('Userauths:signin')  # Redirect back to signin if user not found

        # Authenticate user
        user = authenticate(request, username=user.username, password=password)  # Use 'username' since the default backend requires it
        
        if user is not None:
            login(request, user)
            messages.success(request, 'You are logged in.')
            return redirect('home')
        else:
            messages.warning(request, 'Incorrect password. Please try again.')

    context = {}
    return render(request, 'Userauths/signin.html', context)

def logout_view(request):
  logout(request)
  return redirect('App:home')


