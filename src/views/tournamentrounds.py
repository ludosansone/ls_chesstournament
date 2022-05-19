from core.decorators import menu


class TournamentRoundsView:
    def print_view(datas=None):
        print("Ici, la liste des tours du tournoi")

    @menu("")
    def print_menu(datas=None):
        return [
            {'label': 'Retour aux rapports', 'id': f"logs_controller('{datas.id}')"}
        ]
