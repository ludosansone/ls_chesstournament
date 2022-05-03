from core.validators import is_valid_score


class PlayRoundView:
    def get_first_round_players(players):
        first_round_players = []
        i = 0

        while i < 4:
            player1 = players[i]
            player2 = players[i + 4]
            first_round_players.append(player1)
            first_round_players.append(player2)
            i += 1
        return first_round_players

    def print_view(players):
        round = {}
        matchs = []
        i = 0
        j = 1

        # On organise les matchs selon l'algorithme du système suisse des tournois
        while i < 8:
            player1 = players[i]
            player2 = players[i + 1]
            print(f"Match {j} : {player1.firstname} {player1.lastname} VS {player2.firstname} {player2.lastname}")
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
            i += 2
            j += 1
        round['name'] = "Round 1"
        round['matchs'] = matchs
        return round
