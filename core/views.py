from django.shortcuts import render
from django.views.generic.edit import CreateView
from core.models import Category, Link
from .forms import LinkForm
from django.urls import reverse_lazy

# Create your views here.
def links(request):
    categories= Category.objects.all() 
    links= Link.objects.all()
    return render(request, "core/link_list.html", {'categories':categories,'links':links})


class LinkCreate(CreateView):
    model= Link
    form_class= LinkForm  
    template_name = "core/create.html"

    def get_success_url(self):
        return reverse_lazy('home') + '?created' 