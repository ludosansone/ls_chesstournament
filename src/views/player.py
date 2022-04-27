from core.decorators import menu


@menu("Détail du Joueur")
def player_view(datas=None):
    print(f"{datas['firstname']} {datas['lastname']} ({datas['sexe']})")
    print(f"né le {datas['birthday']}")
    print(f"Classement : {datas['ranking']}\n")

    return [
        {'label': 'Retour à la liste des joueurs', 'id': 'list_players_controller'},
        {'label': 'Retour à la gestion des joueurs', 'id': 'players_controller'},
    ]
