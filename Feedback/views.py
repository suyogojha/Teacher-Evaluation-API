from django.views.generic import TemplateView, CreateView
from .models import FeedbackData


class GetFeedbackView(CreateView):
    model = FeedbackData
    fields = '__all__'
    template_name = 'Feedback/feedback_form.html'


class SuccessView(TemplateView):
    template_name = 'Feedback/success.html'
