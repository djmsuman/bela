from django.urls import include, path

from .views import ItemsView

urlpatterns = [
    path('items/', ItemsView.as_view(), name='items'),
]
