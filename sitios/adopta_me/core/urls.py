from django.urls import path
from . import views as core_views
from rescatados import views as rescatados_views

urlpatterns = [
    path('',core_views.home, name="home"),
    path('about/',core_views.about, name="about"),
    path('visit/',core_views.visit, name="visit"),
    path('rescatados/',rescatados_views.rescatados, name="rescatados"),
]