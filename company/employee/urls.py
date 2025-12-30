
from django.urls import path
from employee import views
app_name="employee"

urlpatterns = [
    path('',views.Home.as_view(),name="home"),
    path('register/',views.Emloyeeregister.as_view(),name="register"),
    path('userlogin/',views.Employeelogin.as_view(),name="userlogin"),
    path('userlogout/',views.Employeelogout.as_view(),name="userlogout"),
    path('detail/<int:i>',views.Employeedetail.as_view(),name="detail"),
    path('edit/<int:i>',views.Employeeupdate.as_view(),name="edit"),
    path('delete/<int:i>',views.Delete.as_view(),name="delete"),
]
