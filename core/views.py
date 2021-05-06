from django.shortcuts import render
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from core.models import Category, Link
from registration.models import Profile
from .forms import LinkForm, CategoryForm, LinkUpdateForm, CategoryUpdateForm
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


class LinkUpdate(UpdateView):
    model= Link
    form_class= LinkUpdateForm 
    template_name = "core/update.html"

    def get_success_url(self):
        return reverse_lazy('home') + '?ok'  


class LinkDelete(DeleteView):
    model= Link
    template_name = "core/confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy('home') + '?deleted'  


class CategoryCreate(CreateView):
    model= Category
    form_class= CategoryForm  
    template_name = "core/create_category.html"

    def get_success_url(self):
        return reverse_lazy('home') + '?createdc' 


class CategoryUpdate(UpdateView):
    model= Category
    form_class= CategoryUpdateForm 
    template_name = "core/update_category.html"

    def get_success_url(self):
        return reverse_lazy('home') + '?ok'  


class CategoryDelete(DeleteView):
    model= Category
    template_name = "core/confirm_delete_category.html"

    def get_success_url(self):
        return reverse_lazy('home') + '?deleted'  

