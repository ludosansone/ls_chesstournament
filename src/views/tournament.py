from core.decorators import menu


@menu("Détail du tournoi")
def tournament_view(datas=None):
    print(f"Nom du tournoi : {datas['name']}")

    print(f"Lieu : {datas['place']}")

    if datas['dates'][0] == datas['dates'][1]:
        print(f"Le : {datas['dates'][0]}")
    else:
        print(f"Du {datas['dates'][0]} au {datas['dates'][1]}")

    return [
        {'label': 'Retour à la liste des tournois', 'id': 'list_tournaments_controller'},
        {'label': 'Retour à la gestion des tournois', 'id': 'tournaments_controller'},
    ]
