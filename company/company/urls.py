"""
URL configuration for company project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from employee import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home.as_view(),name="home"),
    path('register/',views.Emloyeeregister.as_view(),name="register"),
    path('userlogin/',views.Employeelogin.as_view(),name="userlogin"),
    path('userlogout/',views.Employeelogout.as_view(),name="userlogout"),
    path('detail/<int:i>',views.Employeedetail.as_view(),name="detail"),
    path('edit/<int:i>',views.Employeeupdate.as_view(),name="edit"),
    path('delete/<int:i>',views.Delete.as_view(),name="delete"),
]


# for viewing images properly
from django.conf.urls.static import static
from django.conf import settings
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
