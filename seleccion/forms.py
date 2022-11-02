from django import forms


class TeamForm(forms.Form):
    name = forms.CharField(
        label="Nombre de la seleccion",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "seleccion-country",
                "placeholder": "Nombre de la seleccion",
                "required": "True",
            }
        ),
    )
    code = forms.IntegerField(
        label="Ranking:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "selecion-rank",
                "placeholder": "Puesto Ranking",
                "required": "True",
            }
        ),
    )