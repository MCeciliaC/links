"""mylinks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from core import views
from core.views import LinkCreate, LinkUpdate, LinkDelete, CategoryCreate, CategoryUpdate, CategoryDelete
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.links, name='home'),
    path('admin/', admin.site.urls),
    path('create/', login_required(LinkCreate.as_view()), name='create'),
    path('update/<int:pk>/', login_required(LinkUpdate.as_view()), name='update'),
    path('delete/<int:pk>/', login_required(LinkDelete.as_view()), name='delete'),
    path('create_category/', login_required(CategoryCreate.as_view()), name='create_category'),
    path('update_category/<int:pk>/', login_required(CategoryUpdate.as_view()), name='update_category'),
    path('delete_category/<int:pk>/', login_required(CategoryDelete.as_view()), name='delete_category'),

    # Paths de pages
    path('contact/', include('contact.urls')),
    
    # Paths de Auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)