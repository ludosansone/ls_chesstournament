from core.decorators import menu


class PlayersView:
    @menu("Gestion des Joueurs")
    def print_menu(datas=None):
        """
            Affichage du menu de gestion des joueurs
        """

        return [
            {'label': 'Ajouter un Joueur', 'id': 'add_player_controller'},
            {'label': 'lister les Joueurs', 'id': 'list_players_controller'},
            {'label': 'Voir le classement général', 'id': 'general_ranking_controller'},
            {'label': 'Retourner au menu principal', 'id': 'home_controller'},
        ]
