from django.urls import path

from seleccion import views

app_name = "seleccion"
urlpatterns = [
    path("seleccion", views.teams, name="team-list"),
    path("seleccion/add", views.create_team, name="team-add"),
    path("matchgames", views.matchgame, name="matchgame-list"),
]