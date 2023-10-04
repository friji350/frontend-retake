from django.urls import path
from .views import ItemsView, AddView

urlpatterns = [
    path('api/all_items', ItemsView.as_view()),
    path('api/add', AddView.as_view()),
    path('api/delete', AddView.as_view()),
]