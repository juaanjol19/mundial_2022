from datetime import datetime
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from seleccion.forms import TeamForm
from seleccion.models import Team
from seleccion.models import MatchGame


def get_teams(request):
    teams = Team.objects.all()
    paginator = Paginator(teams, 3)
    page_number = request.GET.get("page")
    return paginator.get_page(page_number)


def create_team(request):
    if request.method == "POST":
        team_form = TeamForm(request.POST)
        if team_form.is_valid():
            data = team_form.cleaned_data
            actual_objects = Team.objects.filter(
                country=data["country"], rank=data["rank"]
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"La seleccion de  {data['country']} - {data['rank']} ya está creada",
                )
            else:
                team = Team(name=data["country"], code=data["rank"])
                team.save()
                messages.success(
                    request,
                    f"Seleccion {data['country']} - {data['rank']} creado exitosamente!",
                )

            return render(
                request=request,
                context={"teams": get_teams(request)},
                template_name="seleccion/team_list.html",
            )

    team_form = TeamForm(request.POST)
    context_dict = {"form": team_form}
    return render(
        request=request,
        context=context_dict,
        template_name="seleccion/team_form.html",
    )


def create_matchgame(request, t_local: str, t_away: str,stadium: str,date: str):

    template = loader.get_template("template_matchgame.html")
    due_date = datetime.strptime(due_date, "%Y-%m-%d")
    matchgame = MatchGame(t_local=t_local, t_away=t_away,stadium=stadium,date=date)
    matchgame.save()  # save into the DB

    context_dict = {"matchgame":matchgame}
    render = template.render(context_dict)
    return HttpResponse(render)


def teams(request):
    return render(
        request=request,
        context={"teams": get_teams(request)},
        template_name="seleccion/team_list.html",
    )


def matchgame(request):
    matchgame = MatchGame.objects.all()

    context_dict = {"matchgame":matchgame}

    return render(
        request=request,
        context=context_dict,
        template_name="seleccion/matchgame_list.html",
    )