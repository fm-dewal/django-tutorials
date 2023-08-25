from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    # eg: /polls/
    path(route = "", view = views.index, name = "index"),
    # eg: /polls/2/
    path(route = "<int:question_id>", view = views.detail, name = "detail"),
    # eg: /polls/2/results
    path(route = "<int:question_id>/results", view = views.results, name = "results"),
    # eg: /polls/2/voting
    path(route = "<int:ques_id>/vote", view = views.vote, name = "vote"),
]