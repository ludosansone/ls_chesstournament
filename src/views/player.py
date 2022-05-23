from core.decorators import menu


class PlayerView:
    def print_view(datas):
        """
            Affichage des détails d'un joueur
        """

        print("Détails du joueur\n")
        print(f"{datas.firstname} {datas.lastname} ({datas.sexe})")
        print(f"né le {datas.birthday}")
        print(f"Classement : {datas.ranking}")

    @menu("")
    def print_menu(datas=None):
        """
            Affichage du menu de navigation de la vue
        """

        return [
            {'label': 'Modifier le classement du joueur', 'id': f"change_player_ranking_controller('{datas.id}')"},
            {'label': 'Retour à la liste des joueurs', 'id': 'list_players_controller'},
            {'label': 'Retour à la gestion des joueurs', 'id': 'players_controller'},
        ]
