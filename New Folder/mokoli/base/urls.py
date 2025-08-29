from django.urls import path
from .views import home, signin, signout, signup, adminhome

urlpatterns = [
    path("home/", home, name="home"),
    path("login/", signin, name="login"),
    path("signup/", signup, name="signup"),
    path("logout/", signout, name="logout"),
    path("adminhome/", adminhome, name="adminhome"),
]