"""
URL configuration for ecommerce project.

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
from shop import views
app_name='shop'

urlpatterns = [
    path('',views.CategoryView.as_view(),name='categories'),
    path('products/<int:i>',views.Categoryproducts.as_view(),name='products'),
    path('addcategories/',views.AddCategory.as_view(),name='addcategories'),
    path('addproducts/',views.AddProduct.as_view(),name='addproducts'),
    path('register/',views.Register.as_view(),name="userregister"),
    path('login/',views.Userlogin.as_view(),name="userlogin"),
    path('adminhome/',views.AdminHome.as_view(),name="adminhome"),
    path('userhome/',views.Userhome.as_view(),name="userhome"),
    path('userlogout/',views.Userlogout.as_view(),name="userlogout"),
    path('productdetail/<int:i>/',views.ProductDetail.as_view(),name="productdetail"),
    path('editproduct/<int:i>/',views.Editproduct.as_view(),name="editproduct"),
    path('YourOrders',views.Yourorders.as_view(),name='yourorders'),
]

from django.conf.urls.static import static
from django.conf import settings
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)