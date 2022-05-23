from core.decorators import menu


class ListTournamentsView:
    @menu("Liste des Tournois")
    def print_menu(datas=None):
        """
            Affichage de la liste de tous les tournois
        """

        menu = []

        if datas is not []:
            for tournament in datas:
                new_item_menu = {'label': f"{tournament.name} ({tournament.place})", 'id': tournament.id[0]}
                menu.append(new_item_menu)
        else:
            print("Aucun tournoienregistré\n")
            menu.append({'label': 'Ajouter un tournoi', 'id': 'add_tournament_controller'})

        menu.append({'label': 'Retour à la gestion des tournois', 'id': 'tournaments_controller'})

        return menu
