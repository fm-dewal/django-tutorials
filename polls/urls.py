from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    # eg: /polls/
    # path(route = "", view = views.index, name = "index"),
    path("", views.IndexView.as_view(), name="index"),

    # eg: /polls/2/
    # path(route = "<int:pk>", view = views.detail, name = "detail"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),

    # eg: /polls/2/results
    # path(route = "<int:question_id>/results", view = views.results, name = "results"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),

    # eg: /polls/2/voting
    # path(route = "<int:ques_id>/vote", view = views.vote, name = "vote"),
    path("<int:ques_id>/vote/", views.vote, name="vote"),    
]

