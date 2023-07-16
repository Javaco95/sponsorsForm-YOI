"""
URL configuration for Sponsors project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from form import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('forms/', views.forms, name='forms'),
    path('forms/create/', views.create_form, name='create_form'),
    path('forms/<int:form_id>/', views.form_detail, name='form_detail'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('export-csv/', views.export_csv, name='export_csv'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
