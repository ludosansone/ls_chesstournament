from core.decorators import menu


@menu("Tournoi en cours")
def play_round_view(datas=None):
    print(f"Tour {datas.step}")
    return [
        {'label': 'Retour aux détails du tournoi', 'id': 'tournament_controller',}
    ]
