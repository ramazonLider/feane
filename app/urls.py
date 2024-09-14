from .views import home, menu, about
from django.urls import path


urlpatterns = [
    path('', home, name="home"),
    path('menu/', menu, name="menu"),
    path('about/', about, name="about")
]
