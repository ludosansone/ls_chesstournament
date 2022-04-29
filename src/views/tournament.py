from core.decorators import menu


@menu("Détail du tournoi")
def tournament_view(datas=None):
    print(f"{datas.name}")
    print(f"{datas.place}")
    if datas.dates[0] == datas.dates[1]:
        print(f"Le {datas.dates[0]}")
    else:
        print(f"Du {datas.dates[0]} au {datas.dates[1]}\n")

    if datas.description != "":
        print(f"\n{datas.description}\n")

    print(f"Tournoi en {datas.rounds_number} tours")
    print(f"Contrôle du temps : {datas.time_control}")

    return [
        {'label': 'Retour à la liste des tournois', 'id': 'list_tournaments_controller'},
        {'label': 'Retour à la gestion des tournois', 'id': 'tournaments_controller'},
    ]
