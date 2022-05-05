from core.decorators import menu


class TournamentView:
    def print_tournament_details(tournament):
        print("Détails du Tournoi\n")
        print(f"{tournament.name}")
        print(f"{tournament.place}")
        if tournament.dates[0] == tournament.dates[1]:
            print(f"Le {tournament.dates[0]}")
        else:
            print(f"Du {tournament.dates[0]} au {tournament.dates[1]}\n")

        if tournament.description != "":
            print(f"{tournament.description}\n")

        round = "tour"
        if int(tournament.rounds_number) > 1:
            round = "tours"
        print(f"Tournoi en {tournament.rounds_number} {round}")
        print(f"Contrôle du temps : {tournament.time_control}")

        if tournament.step != "finish":
            print(f"Avancement : Prêt à démarrer le tour {tournament.step}\n")
        else:
            print("Avancement : Tournoi terminé")

    def print_tournament_players(players):
        print("\nParticipants\n")
        players.sort(key=lambda player: int(player.ranking))
        for player in players:
            print(f"{player.firstname} {player.lastname}")

    @menu()
    def print_menu(datas=None):
        menu = []

        if datas.step != "finish":
            menu.append({'label': f"Démarrer le tour {datas.step}", 'id': f"play_round_controller('{datas.id}')"})

        menu.append({'label': 'Retour à la liste des tournois', 'id': 'list_tournaments_controller'})
        menu.append({'label': 'Retour à la gestion des tournois', 'id': 'tournaments_controller'})

        return menu
