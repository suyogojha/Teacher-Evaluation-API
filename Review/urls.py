from django.urls import path
from .views import ListFeedbackView, SearchResultsView, deleteAllFeedback, FeedbackDetailView, DeleteFeedbackView

urlpatterns = [
    path('', ListFeedbackView.as_view(), name='ListFeedbackView'),
    path('search/', SearchResultsView.as_view(), name='SearchResultsView'),
    path('delete/', deleteAllFeedback, name='deleteAllFeedback'),
    path('feedback/<int:pk>/', FeedbackDetailView.as_view(), name='FeedbackDetailView'),
    path('feedback/<int:pk>/delete/', DeleteFeedbackView.as_view(), name='DeleteFeedbackView')
]
