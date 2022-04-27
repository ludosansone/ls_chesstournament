from core.decorators import menu


@menu("Gestion des Tournois")
def tournaments_view(datas=None):
    return [
        {'label': 'Ajouter un Tournoi', 'id': 'add_tournament_controller'},
        {'label': 'lister les Tournois', 'id': 'list_tournaments_controller'},
        {'label': 'Retourner au menu principal', 'id': 'home_controller'},
    ]
