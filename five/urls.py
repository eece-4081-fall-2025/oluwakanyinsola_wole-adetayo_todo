from django.urls import path
from . import views
app_name = "five"
urlpatterns = [
path("", views.index, name="index"),
]
