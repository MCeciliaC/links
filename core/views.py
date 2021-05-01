from django.shortcuts import render
from core.models import Category, Link

# Create your views here.
def links(request):
    categories= Category.objects.all() 
    links= Link.objects.all()
    return render(request, "core/link_list.html", {'categories':categories,'links':links})
