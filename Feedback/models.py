from django.db import models
from django.urls import reverse
from Home.models import Teacher


class FeedbackData(models.Model):

    CHOICES = (
        ('Strongly Disagree', 'Strongly Disagree'),
        ('Disagree', 'Disagree'),
        ('Sometimes', 'Sometimes'),
        ('Agree', 'Agree'),
        ('Strongly Agree', 'Strongly Agree'),
    )

    date_submitted = models.DateTimeField(auto_now=True)

    teacher_name = models.ForeignKey(Teacher, verbose_name='Name of Teacher',
                                     on_delete=models.CASCADE)

    punctuality = models.CharField(verbose_name='The teacher is punctual in coming to class',
                                   max_length=225,
                                   choices=CHOICES)

    portion = models.CharField(verbose_name='The teacher completes portions at the appropriate time',
                               max_length=225,
                               choices=CHOICES)

    doubt = models.CharField(verbose_name='The teacher takes in effort to clear your doubts',
                             max_length=225,
                             choices=CHOICES)

    interactive = models.CharField(verbose_name='The teacher makes the class interactive',
                                   max_length=225,
                                   choices=CHOICES)

    comments = models.TextField(verbose_name='Any other feedback (your comments)',
                                blank=True)

    class Meta:
        verbose_name = 'Feedback Data'
        verbose_name_plural = 'Feedback Data'

    def __str__(self):
        return self.teacher_name.name

    def get_absolute_url(self):
        return reverse('SuccessView')
