from core.decorators import menu


class TournamentsView:
    @menu("Gestion des Tournois")
    def print_menu(datas=None):
        """
            Affichage du menu de gestion des tournois
        """

        return [
            {'label': 'Ajouter un Tournoi', 'id': 'add_tournament_controller'},
            {'label': 'lister les Tournois', 'id': 'list_tournaments_controller'},
            {'label': 'Retourner au menu principal', 'id': 'home_controller'},
        ]
