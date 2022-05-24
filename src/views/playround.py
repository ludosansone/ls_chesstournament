from core.validators import is_valid_score
from datetime import datetime


class PlayRoundView:
    def print_view(players):
        """
            Affichage du déroulement d'un des tours du tournoi
        """

        round = {}
        round['begin'] = str(datetime.now())
        matchs = []
        i = 0
        j = 1

        # On déroule les matchs selon l'algorithme du système suisse des tournois
        while i < 8:
            player1 = players[i]
            player2 = players[i + 1]
            print(f"Match {j} : {player1.firstname} {player1.lastname} VS {player2.firstname} {player2.lastname}")
            while True:
                score_player1 = input(f"Saisissez le score de {player1.firstname} {player1.lastname} (0, 1, 0.5) : ")
                if is_valid_score(score_player1) is True:
                    break
            while True:
                score_player2 = input(f"Saisissez le score de {player2.firstname} {player2.lastname} : ")
                if is_valid_score(score_player2) is True:
                    break
            match_list_1 = [
                player1.id,
                score_player1,
            ]
            match_list_2 = [
                player2.id,
                score_player2,
            ]
            match = (match_list_1, match_list_2)
            matchs.append(match)
            i += 2
            j += 1
        round['matchs'] = matchs
        round['end'] = str(datetime.now())
        return round
