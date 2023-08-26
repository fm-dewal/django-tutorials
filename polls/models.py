import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("published_date")

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return (self.pub_date >= timezone.now() - datetime.timedelta(days=1)) == \
            (self.pub_date < timezone.now())
    
    class Meta:
        ordering = ["-pub_date"] #descending

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=200)
    tally = models.IntegerField(default=0)

    def __str__(self):
        return self.choice
