from django.urls import path
from .views import HomeView, get_teachers

urlpatterns = [
    path('', HomeView.as_view(), name='HomeView'),
    path('ajax_calls/autocomplete_search_func', get_teachers, name='get_teachers'),
]
