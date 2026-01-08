
from django.urls import path
from app  import views
app_name='app'

urlpatterns = [
    path('',views.Home.as_view(),name="home"),
    path('register/',views.Register.as_view(),name="register"),
    path('login/',views.Userlogin.as_view(),name="userlogin"),
    path('adminhome/',views.Adminhome.as_view(),name="adminhome"),
    path('studenthome/',views.Studenthome.as_view(),name="studenthome"),
    path('userlogout/',views.Userlogout.as_view(),name="userlogout"),
    path('addschool/',views.Addschool.as_view(),name="addschool"),

]