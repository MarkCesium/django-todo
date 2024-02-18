from django.urls import path
from .views import index, update_task, delete_task


urlpatterns = [
    path("", index, name="index"),
    path("update_task/<int:pk>", update_task, name="update_task"),
    path("delete_task/<int:pk>", delete_task, name="delete_task")
]
