from django.urls import path
from . import views


# localhost = 8000/test_home
# localhost = 8000/test_home/orders
urlpatterns = [
    path("", views.test_home, name="test_home"), 
]