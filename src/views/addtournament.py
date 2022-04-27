from core.decorators import menu


@menu("Ajouter un Tournoi")
def add_tournament_view(datas=None):
    print("Ici, le formulaire d'ajout d'un tournoi")
    return [
        {'label': 'Retour à la gestion des tournois', 'id': 'tournaments_controller'}
    ]
