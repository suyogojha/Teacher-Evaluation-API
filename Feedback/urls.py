from django.urls import path
from .views import GetFeedbackView, SuccessView

urlpatterns = [
    path('', GetFeedbackView.as_view(), name='GetFeedbackView'),
    path('success/', SuccessView.as_view(), name='SuccessView'),
]
