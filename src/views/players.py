from core.decorators import menu


@menu("Gestion des Joueurs")
def players_view(datas=None):
    return [
        {'label': 'Ajouter un Joueur', 'id': 'add_player_controller'},
        {'label': 'lister les Joueurs', 'id': 'list_players_controller'},
        {'label': 'Retourner au menu principal', 'id': 'home_controller'},
    ]
