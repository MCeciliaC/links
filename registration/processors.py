from .models import Profile
from django.contrib.auth import get_user_model

def profile(request):
    profiles= Profile.objects.all()
    return {'profiles': profiles}

