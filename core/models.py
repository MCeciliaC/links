from django.db import models
from registration.models import Profile

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name= "Categoría")
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True) 

    class Meta:
        verbose_name= "Categoría"
    
    def __str__(self):
        return self.name

class Link(models.Model):
    name = models.CharField( max_length=100, verbose_name= "Sitio")
    text = models.TextField(null=True, blank=True, verbose_name= "Descripción") 
    link = models.URLField(verbose_name= "Url", default=None, max_length=500, null=True, blank=True)
    img= models.ImageField(verbose_name= "Imagen", upload_to="logo", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True) 
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True) 

    class Meta:
        verbose_name= "Sitio"
    
    def __str__(self):
        return self.name
