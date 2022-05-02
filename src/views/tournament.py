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

        print(f"Tournoi en {tournament.rounds_number} tours")
        print(f"Contrôle du temps : {tournament.time_control}")
        if tournament.step == "1":
            print("Avancement : Prêt à démarrer le premier tour\n")

    def print_tournament_players(players):
        print("\nParticipants\n")
        players.sort(key=lambda player: player.lastname)
        for player in players:
            print(f"{player.firstname} {player.lastname}")

    @menu()
    def print_menu(datas=None):
        menu = []

        if datas.step == "1":
            menu.append({'label': 'Démarrer le premier tour', 'id': f"play_round_controller('{datas.id}')"})

        menu.append({'label': 'Retour à la liste des tournois', 'id': 'list_tournaments_controller'})
        menu.append({'label': 'Retour à la gestion des tournois', 'id': 'tournaments_controller'})

        return menu
