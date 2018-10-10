from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import Profile

class ProfileCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Profile
        fields = ('username', 'password')

class EditProfileForm(UserChangeForm):

    class Meta:
        model = Profile
        fields = ('email','password')
        excludes = ('password')
    email = forms.CharField(label="Email", max_length=30, 
                               widget=forms.EmailInput(attrs={'class': 'form-control', 'name': 'email', 'placeholder': 'enter email...'}))

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username', 'placeholder': 'Username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password', 'placeholder': 'Password'}))
                            
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Profile
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user
    
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username', 'placeholder': 'Username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'first_name', 'placeholder': 'Prenom'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'last_name', 'placeholder': 'Nom'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'name': 'email', 'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password1', 'placeholder': 'Mot de passe'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password2', 'placeholder': 'Confirmer votre mot de passe'}))