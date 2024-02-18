from django.urls import path
from .views import index, update_task


urlpatterns = [
    path("", index, name="index"),
    path("update_task/<int:pk>", update_task, name="update_task"),
]
