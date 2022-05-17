from core.decorators import menu


class ListPlayersView:
    @menu("Liste des Joueurs")
    def print_menu(players=None):
        menu = []

        if players is not []:
            for player in players:
                new_item_menu = {'label': f"{player.firstname} {player.lastname}", 'id': player.id[0]}
                menu.append(new_item_menu)
        else:
            print("Aucun joueur enregistré\n")
            menu.append({'label': 'Ajouter un joueur', 'id': 'add_player_controller'})

        menu.append({'label': 'Retour à la gestion des joueurs', 'id': 'players_controller'})

        return menu
