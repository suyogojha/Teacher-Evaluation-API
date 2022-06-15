from django.contrib import admin
from .models import FeedbackData


class FeedbackDataAdmin(admin.ModelAdmin):
    autocomplete_fields = ['teacher_name']


admin.site.register(FeedbackData, FeedbackDataAdmin)
