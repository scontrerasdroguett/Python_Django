from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('about/',views.about, name="about"),
    path('visit/',views.visit, name="visit"),
    path('rescatados/',views.rescatados, name="rescatados"),
]