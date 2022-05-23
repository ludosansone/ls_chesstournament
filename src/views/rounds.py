from core.decorators import menu
from core.transformators import get_smart_date_time
from models.player import Player


class RoundsView:
    def print_rounds(rounds):
        """
            Affichage de tous les tours terminés d'un tournoi, avec tous leurs détails
        """

        for round in rounds:
            match_number = 0
            print(f"\n{round.name}")
            print(f"Début : {get_smart_date_time(round.begin)}")
            print(f"Fin :   {get_smart_date_time(round.end)}")
            while match_number < 4:
                player1_id = round.matchs[match_number][0][0]
                player1_score = round.matchs[match_number][0][1]
                player2_id = round.matchs[match_number][1][0]
                player2_score = round.matchs[match_number][1][1]
                player1 = Player.read(player1_id)
                player2 = Player.read(player2_id)
                print(f"Match {match_number + 1}")
                print(f"{player1.firstname} {player1.lastname} : {player1_score} ", end='')
                print(f"{player2.firstname} {player2.lastname} : {player2_score}")
                match_number += 1

    @menu()
    def print_menu(param=None):
        """
            Affichage du menu de navigation de la vue
        """

        return [
            {'label': 'Retour au détails du tournoi', 'id': f"tournament_controller('{param}')"}
        ]
