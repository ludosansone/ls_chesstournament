from core.decorators import menu


class PlayersRankingOrderView:
    def print_view(players):
        print("Liste des joueurs du tournoi (par ordre de classement)\n")

        for player in players:
            print(f"{player.firstname} {player.lastname}")

    @menu("")
    def print_menu(datas=None):
        return [
            {'label': 'Retour aux rapports', 'id': f"logs_controller('{datas.id}')"}
        ]
