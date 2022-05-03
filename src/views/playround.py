from core.validators import is_valid_score


class PlayRoundView:
    def print_view(datas=None):
        round = {}
        matchs = []
        i = 0

        # On organise les matchs selon l'algorithme du système suisse des tournois
        while i < 4:
            player1 = datas[i]
            player2 = datas[i + 4]
            print(f"Match {i + 1} : {player1.firstname} {player1.lastname} VS {player2.firstname} {player2.lastname}")
            while True:
                score_player1 = input(f"Saisissez le score de {player1.firstname} {player1.lastname} : ")
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
            i += 1
        round['name'] = "Round 1"
        round['matchs'] = matchs
        return round
