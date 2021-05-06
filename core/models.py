from django.db import models
from registration.models import Profile

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name= "Categoría", null=False, blank=False) 
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=False, blank=False) 

    class Meta:
        verbose_name= "Categoría"
    
    def __str__(self):
        return self.name

class Link(models.Model):
    name = models.CharField( max_length=100, verbose_name= "Sitio", null=False, blank=False) 
    text = models.TextField(verbose_name= "Descripción corta", null=True, blank=True)  
    link = models.URLField(verbose_name= "Url", default=None, max_length=500, null=False, blank=False) 
    img= models.ImageField(verbose_name= "Imagen", upload_to="logo", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False) 
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=False, blank=False) 

    class Meta:
        verbose_name= "Sitio"
    
    def __str__(self):
        return self.name


