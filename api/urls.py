from django.urls import path

from .views import ItemNotificationStatusView, ItemsView

urlpatterns = [
    path("items/", ItemsView.as_view(), name="items"),
    path(
        "items/notify/<str:task_id>/",
        ItemNotificationStatusView.as_view(),
        name="item-notify-status",
    ),
]
