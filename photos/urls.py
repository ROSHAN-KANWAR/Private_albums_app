from django.contrib import admin
from django.urls import path
from photos import views
urlpatterns = [
    path("",views.Gallery,name="gallery"),
    path("photoview/<int:pk>", views.Viewphoto, name="viewphoto"),
    path("addphoto/",views.Addphoto,name="addphoto"),
    path("loginuser/",views.Loginuser,name="login"),
    path("logout/",views.Logoutuser,name="logout"),
    path("createaccount/",views.Register,name="register")
]
