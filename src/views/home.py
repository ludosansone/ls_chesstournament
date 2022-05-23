from core.decorators import menu


class HomeView:
    @menu("Menu Principal")
    def print_menu(datas=None):
        """
            Affichage du menu principal
        """

        return [
            {'label': 'Gestion des Joueurs', 'id': 'players_controller'},
            {'label': 'Gestion des Tournois', 'id': 'tournaments_controller'},
            {'label': 'Quitter le programme', 'id': 'exit_controller'},
        ]
