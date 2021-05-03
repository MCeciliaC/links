from .models import Profile
from core.models import Category
from django.contrib.auth import get_user_model

def profile(request):
    profiles= Profile.objects.all()
    categories= Category.objects.all() 
    return {'profiles': profiles, 'categories': categories}

