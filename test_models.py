from polls.models import Question, Choice
from djangoSite import settings
from django.utils import timezone
import time

def tryOne():
    Question.objects.all()
    q = Question(question_text = "What's new?", pub_date = timezone.now())
    q.save()
    print(q.id)

    print(q.question_text)
    print(q.pub_date)

    q.question_text = "What's up?" + str(q.id)
    q.save()

    print(Question.objects.all())

    print(Question.objects.filter(id = 1))
    print(Question.objects.filter(question_text__startswith = "What"))

    curr_year = timezone.now().year
    
    # Error if more than one rows/ objects returned
    # Question.objects.get(pub_date__year = curr_year)
    
    print(Question.objects.filter(pub_date__year = curr_year))
    
    print(Question.objects.filter(id = 2))
    
    # Avoiding re-assignment of variable 'q'
    #   Choices to be linked with latest question created upon multiple runs :)
    # q = Question.objects.get(pk = 1)
    # if q == None:
    #     q = Question.objects.get(question_text__startswith = "What")
    # print(q.was_published_recently())

    print(q.choice_set.all())

    c1 = q.choice_set.create(choice = "Nothing much", tally = 0)
    c2 = q.choice_set.create(choice = "The sky", tally = 0)
    c3 = q.choice_set.create(choice = "Just hacking for fun", tally = 1)

    print(c1, c2, c3)
    print("sleep for 2s")

    print(c1.question, c2.question, c3.question)

    print(q.choice_set.all())
    print(q.choice_set.count())

    print(Choice.objects.filter(question__pub_date__year = curr_year))

    c = q.choice_set.filter(choice__startswith = "Just hacking")
    c.delete()
    
tryOne()






