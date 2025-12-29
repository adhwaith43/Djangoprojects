"""
URL configuration for library project.

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
from django.urls import path
from books import views
app_name ='books'

urlpatterns = [
    # path('',views.home,name="home"), # function based path

    path('',views.Home.as_view(),name="home"), # class based path

    # path('viewbooks/',views.viewBooks,name="viewbooks"),
    path('viewbooks/',views.ViewBooks.as_view(),name="viewbooks"),

    # path('addbooks/',views.addBooks,name="addbooks"),
    path('addbooks/',views.AddBooks.as_view(),name="addbooks"),

    # path('detail/<int:i>',views.detail,name="detail"),
    path('detail/<int:i>',views.Detail.as_view(),name="detail"),

    # path('delete/<int:i>',views.delete,name="delete"),
    path('delete/<int:i>',views.Delete.as_view(),name="delete"),

    # path('edit/<int:i>',views.edit,name="edit")
    path('edit/<int:i>',views.Edit.as_view(),name="edit")
]

