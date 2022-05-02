from core.decorators import menu


@menu("Détail du tournoi")
def tournament_view(datas=None):
    menu = []

    print(f"{datas['tournament'].name}")
    print(f"{datas['tournament'].place}")
    if datas['tournament'].dates[0] == datas['tournament'].dates[1]:
        print(f"Le {datas['tournament'].dates[0]}")
    else:
        print(f"Du {datas['tournament'].dates[0]} au {datas['tournament'].dates[1]}\n")

    if datas['tournament'].description != "":
        print(f"{datas['tournament'].description}\n")

    print(f"Tournoi en {datas['tournament'].rounds_number} tours")
    print(f"Contrôle du temps : {datas['tournament'].time_control}")

    print("\nParticipants\n")
    datas['players'].sort(key = lambda player : player.lastname)
    for player in datas['players']:
        print(f"{player.firstname} {player.lastname}")
    print("")

    if datas['tournament'].step == "1":
        print("Avancement : Prêt à démarrer le premier tour\n")
        menu.append({'label': 'Démarrer le premier tour', 'id': f"play_round_controller('{datas['tournament'].id}')"})

    menu.append({'label': 'Retour à la liste des tournois', 'id': 'list_tournaments_controller'})
    menu.append({'label': 'Retour à la gestion des tournois', 'id': 'tournaments_controller'})

    return menu
