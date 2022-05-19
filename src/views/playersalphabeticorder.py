from core.decorators import menu


class PlayersAlphabeticOrderView:
    def print_view(players):
        print("Joueurs du tournoi (Par ordre alphabétique de leur nom de famille)\n")

        for player in players:
            print(f"{player.firstname} {player.lastname}")

    @menu("")
    def print_menu(datas=None):
        return [
            {'label': 'Retour aux rapports', 'id': f"logs_controller('{datas.id}')"}
        ]
