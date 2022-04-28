from core.decorators import menu


@menu("Liste des Joueurs")
def list_players_view(datas=None):
    menu = []

    if datas is not []:
        for player in datas:
            new_item_menu = {'label': f"{player.firstname} {player.lastname}", 'id': player.id[0]}
            menu.append(new_item_menu)
    else:
        print("Aucun joueur enregistré\n")
        menu.append({'label': 'Ajouter un joueur', 'id': 'add_player_controller'})

    menu.append({'label': 'Retour à la gestion des joueurs', 'id': 'players_controller'})

    return menu
