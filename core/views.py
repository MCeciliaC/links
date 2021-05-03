from django.shortcuts import render
from django.views.generic.edit import CreateView
from core.models import Category, Link
from registration.models import Profile
from .forms import LinkForm, CategoryForm
from django.urls import reverse_lazy

# Create your views here.
def links(request):    
    links= Link.objects.all()
    return render(request, "core/link_list.html", {'links':links})


class LinkCreate(CreateView):
    model= Link
    form_class= LinkForm  
    template_name = "core/create.html"

    def get_success_url(self):
        return reverse_lazy('home') + '?created' 

class CategoryCreate(CreateView):
    model= Category
    form_class= CategoryForm  
    template_name = "core/create_category.html"

    def get_success_url(self):
        return reverse_lazy('home') + '?created' 