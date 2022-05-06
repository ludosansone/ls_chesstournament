from core.decorators import menu


class GeneralRankingView:
    @menu("Classement Général")
    def print_menu(datas):
        for player in datas:
            print(f"{player.firstname} {player.lastname} : {player.ranking}")

        return [
            {'label': 'Retour à la gestion des joueurs', 'id': 'players_controller'}
        ]
