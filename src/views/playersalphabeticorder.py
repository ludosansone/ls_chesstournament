from core.decorators import menu


class PlayersAlphabeticOrderView:
    def print_view(players):
        """
            Affichage de la liste des joueurs d'un tournoi, par ordre alphabétique
        """

        print("Joueurs du tournoi (Par ordre alphabétique de leur nom de famille)\n")

        for player in players:
            print(f"{player.firstname} {player.lastname}")

    @menu("")
    def print_menu(datas=None):
        """
            Affichage du menu de navigation de la vue
        """

        return [
            {'label': 'Retour aux rapports', 'id': f"logs_controller('{datas.id}')"}
        ]
