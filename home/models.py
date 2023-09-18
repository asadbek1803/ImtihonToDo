from django.db import models

# Create your models here.

class Todo(models.Model):
    status_s = (
        ['bajarilmoqda', 'Bajarilmoqda'],
        ['tugatildi', 'Tugatildi'],
        ['to\'xtadi','To\'xtadi']
    )
    title = models.CharField(max_length=150)
    time = models.DateTimeField()
    description = models.TextField()
    status = models.CharField(max_length=4, choices=status_s)


