from django import forms
from .models import FacilityInput

class FacilityInputForm(forms.ModelForm):
    """
    Form for creating and updating FacilityInput instances.
    """

    class Meta:
        model = FacilityInput
        fields = [
            'facility_ownership',
            'facility_name',
            'address',
            'state',
            'lga',
            'director_title',
            'director_name',
            'phone_number',
            'email',
            'nin',
            'facility_type',
            'password',
            'serial_code'
        ]
        
        # Adding custom labels, help texts, and widgets if necessary
        labels = {
            'facility_ownership': 'Facility Ownership',
            'facility_name': 'Facility Name',
            'address': 'Address',
            'state': 'State',
            'lga': 'LGA',
            'director_title': 'Director Title',
            'director_name': 'Director Name',
            'phone_number': 'Phone Number',
            'email': 'Email Address',
            'nin': 'National Identification Number (NIN)',
            'facility_type': 'Facility Type',
            'password': 'Password',
            'serial_code': 'Facility Serial Code',
        }
        
        help_texts = {
            'facility_name': 'Enter the full name of the facility.',
            'email': 'This must be a unique email address.',
            'nin': 'Enter the National Identification Number.',
        }

        widgets = {
            'facility_ownership': forms.Select(attrs={'class': 'form-control'}),
            'facility_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'lga': forms.Select(attrs={'class': 'form-control'}),
            'director_title': forms.Select(attrs={'class': 'form-control'}),
            'director_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'nin': forms.TextInput(attrs={'class': 'form-control'}),
            'facility_type': forms.Select(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'serial_code': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if FacilityInput.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email

    def clean_nin(self):
        nin = self.cleaned_data.get('nin')
        if FacilityInput.objects.filter(nin=nin).exists():
            raise forms.ValidationError("This NIN is already in use.")
        return nin

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 6:
            raise forms.ValidationError("Password must be at least 6 characters long.")
        return password


class SignInForm(forms.Form):
    facility_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Facility Name'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
