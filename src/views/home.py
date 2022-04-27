from core.decorators import menu


@menu("Menu Principal")
def home_view(datas=None):
    return [
        {'label': 'Gestion des Joueurs', 'id': 'players_controller'},
        {'label': 'Gestion des Tournois', 'id': 'tournaments_controller'},
        {'label': 'Quitter le programme', 'id': 'exit_controller'},
    ]
