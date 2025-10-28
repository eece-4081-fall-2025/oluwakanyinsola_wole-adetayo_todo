from django.urls import path
from . import views
app_name = "five"
urlpatterns = [
path("", views.index, name="index"),
path("create/", views.task_create, name="task_create"),
path("<int:pk>/edit/", views.task_edit, name="task_edit"),
path("<int:pk>/delete/", views.task_delete, name="task_delete"),
path("<int:pk>/toggle/", views.task_toggle, name="task_toggle"),
path("<int:pk>/move/<str:direction>/", views.task_move, name="task_move"),
]
