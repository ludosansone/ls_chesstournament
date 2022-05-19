from core.decorators import menu


class PlayersAlphabeticOrderView:
    def print_view(datas=None):
        print("Ici, la liste des joueurs du tournoi par ordre alphabétique")

    @menu("")
    def print_menu(datas=None):
        return [
            {'label': 'Retour aux rapports', 'id': f"logs_controller('{datas.id}')"}
        ]
