from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import ProfileCreationForm, EditProfileForm
from .models import Profile

class ProfileAdmin(UserAdmin):
    add_form = ProfileCreationForm
    form = EditProfileForm
    model = Profile
    list_display = ['email', 'username',]

admin.site.register(Profile, ProfileAdmin)