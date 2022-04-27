from core.decorators import menu


@menu("Liste des Tournois")
def list_tournaments_view(datas=None):
    menu = []
    if datas != []:
        for tournament in datas:
            new_item_menu = {'label': tournament['name'], 'id': tournament['id']}
            menu.append(new_item_menu)
    else:
        print("Aucun tournoi enregistré\n")
        menu.append({'label': 'Ajouter un tournoi', 'id': 'add_tournament_controller'})

    menu.append({'label': 'Retour à la gestion des tournois', 'id': 'tournaments_controller'})

    return menu
