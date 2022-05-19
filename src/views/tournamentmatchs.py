from core.decorators import menu


class TournamentMatchsView:
    def print_view(datas=None):
        print("Ici, la liste des matchs du tournoi")

    @menu("")
    def print_menu(datas=None):
        return [
            {'label': 'Retour aux rapports', 'id': f"logs_controller('{datas.id}')"}
        ]
