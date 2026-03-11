from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
#we use the NewUserCreationForm created in form.py which is inherited from UserCreationForm
from .forms import NewUserCreationForm

def register(request):
    if request.method == 'POST':
        # user submit the form and put data into NewUserCreationForm
        form = NewUserCreationForm(request.POST)
        if form.is_valid():
            #after proof passed, store new user and redirect to login page
            form.save()
            return redirect('accounts:login')
        # if validation failure, continue to render the register page
    else:
        # When user open the page, give them an empty page
        form = NewUserCreationForm()

    # GET or POST failure，then render the register page again
    return render(request, 'accounts/register.html', {'form': form})

