from core.decorators import menu


class PlayerView:
    def print_view(datas):
        print(f"{datas.firstname} {datas.lastname} ({datas.sexe})")
        print(f"né le {datas.birthday}")
        print(f"Classement : {datas.ranking}\n")

    @menu("Détail du Joueur")
    def print_menu(datas=None):
        return [
            {'label': 'Retour à la liste des joueurs', 'id': 'list_players_controller'},
            {'label': 'Retour à la gestion des joueurs', 'id': 'players_controller'},
        ]
