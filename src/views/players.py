from core.decorators import menu


class PlayersView:
    @menu("Gestion des Joueurs")
    def print_menu(datas=None):
        return [
            {'label': 'Ajouter un Joueur', 'id': 'add_player_controller'},
            {'label': 'lister les Joueurs', 'id': 'list_players_controller'},
            {'label': 'Retourner au menu principal', 'id': 'home_controller'},
        ]
