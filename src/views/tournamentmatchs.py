from core.decorators import menu
from models.player import Player


class TournamentMatchsView:
    def print_view(rounds):
        """
            Affichage de tous les matchs terminés d'un trounoi
        """

        i = 1

        for round in rounds:
            match_number = 0
            while match_number < 4:
                player1_id = round.matchs[match_number][0][0]
                player1_score = round.matchs[match_number][0][1]
                player2_id = round.matchs[match_number][1][0]
                player2_score = round.matchs[match_number][1][1]
                player1 = Player.read(player1_id)
                player2 = Player.read(player2_id)
                print(f"{i} - {player1.firstname} {player1.lastname} : {player1_score} ", end='')
                print(f"{player2.firstname} {player2.lastname} : {player2_score}")
                match_number += 1
                i += 1

    @menu("")
    def print_menu(datas=None):
        """
            Affichage du menu de navigation de la vue
        """

        return [
            {'label': 'Retour aux rapports', 'id': f"logs_controller('{datas.id}')"}
        ]
