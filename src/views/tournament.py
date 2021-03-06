from core.decorators import menu


class TournamentView:
    def print_tournament_details(tournament):
        """
            Affichage de tous les détails d'un tournoi
        """

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
            print("Avancement : Tournoi terminé\n")

    def print_ranking(players, step):
        """
            Affichage du classement actualisé d'un tournoi
        """

        if step == "1":
            print("Participants\n")
        elif step == "finish":
            print("Classement Final\n")

        for player in players:
            print(f"{player.firstname} {player.lastname}")

    def print_futur_matchs(players):
        """
            Affichage des matchs devant être disputés au prochain tour
        """

        i = 0
        print("Matchs à venir\n")

        while i < 7:
            print(f"{players[i].firstname} {players[i].lastname} VS ", end='')
            print(f"{players[i + 1].firstname} {players[i + 1].lastname}")
            i += 2

    @menu()
    def print_menu(datas=None):
        """
            Affichage du menu de navigation de la vue
        """

        menu = []

        if datas.step != "finish":
            menu.append({'label': f"Démarrer le tour {datas.step}", 'id': f"play_round_controller('{datas.id}')"})

        if datas.step != "1":
            menu.append({'label': 'Voir le détail des tours terminés', 'id': f"rounds_controller('{datas.id}')"})
            menu.append({'label': 'Rapports', 'id': f"logs_controller('{datas.id}')"})

        menu.append({'label': 'Retour à la liste des tournois', 'id': 'list_tournaments_controller'})
        menu.append({'label': 'Retour à la gestion des tournois', 'id': 'tournaments_controller'})

        return menu
