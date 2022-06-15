from django.db import models


class Teacher(models.Model):
    name = models.CharField(verbose_name='Name of teacher',
                            max_length=255, unique=True)

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

    def __str__(self):
        return self.name
