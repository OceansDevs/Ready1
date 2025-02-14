from django.shortcuts import render, redirect
from .forms import FacilityInputForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from .forms import SignInForm
from .models import Facility, FacilityInput
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm

# from .forms import SigninForm

def home(request):
    return render(request, 'app/home.html')


def signup(request):
    if request.method == 'POST':
        form = FacilityInputForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')  # Redirect after successful form submission
    else:
        form = FacilityInputForm()

    return render(request, 'app/signup.html', {'form': form})




def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            facility_name = form.cleaned_data['facility_name']
            password = form.cleaned_data['password']
            
            try:
                # Find the facility based on the provided facility name
                facility = FacilityInput.objects.get(facility_name=facility_name)
                
                # Check if the password matches
                if check_password(password, facility.password):
                    # If the password is correct, log the user in or perform any other action
                    # For this example, we will simply redirect to a 'dashboard' page
                    return redirect('facility_profile', facility_id=facility.id)
                else:
                    messages.error(request, 'Invalid password. Please try again.')
            
            except FacilityInput.DoesNotExist:
                messages.error(request, 'Facility not found. Please check the facility name.')

    else:
        form = SignInForm()

    return render(request, 'app/signin.html', {'form': form})





def profile_view(request, facility_id):
    # Retrieve the FacilityInput object by its ID
    facility = get_object_or_404(FacilityInput, id=facility_id)

    if request.method == 'POST':
        # Create a form instance with POST data
        form = FacilityInputForm(request.POST, instance=facility)
        if form.is_valid():
            # Save the updated facility data
            form.save()
            # Optionally, redirect to a success page (or back to the profile)
            return redirect('facility_profile', facility_id=facility.id)
    else:
        # If GET request, use the form pre-filled with the facility data
        form = FacilityInputForm(instance=facility)

    # Render the profile page with the form
    return render(request, 'app/profile.html', {'form': form, 'facility': facility})


@login_required
def edit_profile(request, facility):
    if request.method == "POST":
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('facility_profile', facility_id=facility.id) # type: ignore # Change 'profile' to your actual profile view name
    else:
        form = UserChangeForm(instance=request.user)
    
    return render(request, "edit_profile.html", {"form": form})
