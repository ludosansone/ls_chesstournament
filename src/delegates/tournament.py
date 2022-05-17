from models.player import Player


def get_first_peers(tournament):
    list_players = []
    i = 0

    while i < 4:
        player1 = tournament.players[i]
        player2 = tournament.players[i + 4]
        list_players.append(player1)
        list_players.append(player2)
        i += 1
    return list_players

def get_all_scores(rounds):
    round_index = 0
    list_players = []

    while round_index < len(rounds):
        match_number = 0
        while match_number < 4:
            player1_id = rounds[round_index].matchs[match_number][0][0]
            player1_score = float(rounds[round_index].matchs[match_number][0][1])
            player1 = Player.read(player1_id)
            player1_ranking = player1.ranking
            player2_id = rounds[round_index].matchs[match_number][1][0]
            player2_score = float(rounds[round_index].matchs[match_number][1][1])
            player2 = Player.read(player2_id)
            player2_ranking = player2.ranking
            player_found = False
            player_index = 0
            while player_index < len(list_players):
                if list_players[player_index]['player_id'] == player1_id:
                    new_score = float(list_players[player_index]['score']) + player1_score
                    player = {'player_id': player1_id, 'score': str(new_score), 'ranking': player1_ranking}
                    list_players[player_index] = player
                    player_found = True
                elif list_players[player_index]['player_id'] == player2_id:
                    new_score = float(list_players[player_index]['score']) + player2_score
                    player = {'player_id': player2_id, 'score': str(new_score), 'ranking': player2_ranking}
                    list_players[player_index] = player
                    player_found = True
                player_index += 1
            if player_found is False and round_index == 0:
                list_players.append({'player_id': player1_id, 'score': player1_score, 'ranking': player1_ranking})
                list_players.append({'player_id': player2_id, 'score': player2_score, 'ranking': player2_ranking})
            match_number += 1
        round_index += 1
    return list_players

def compare(p1, p2):
    """
        Fonction auxilière, permettant la constitution des paires de joueurs à partir du second tour
    """

    if p1['score'] > p2['score']:
        return -1
    elif p1['score'] < p2['score']:
        return 1
    else:
        if p1['ranking'] > p2['ranking']:
            return 1
        elif p1['ranking'] < p2['ranking']:
            return -1
        else:
            return 0
