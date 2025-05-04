from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page='login'), name="logout"),
    path("", view=TaskList.as_view(), name='tasks'),
    path("task/<int:pk>", view=TaskDetail.as_view(), name="details"),
    path("create-task/", view=TaskCreate.as_view(), name="task-create"),
    path("edit-task/<int:pk>", TaskUpdate.as_view(), name="task-update"),
    path("delete-task/<int:pk>", TaskDelete.as_view(), name="task-delete")
]
