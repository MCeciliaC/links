from django.contrib import admin
from .models import Category, Link

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    pass

class LinkAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin) 
admin.site.register(Link, LinkAdmin) 