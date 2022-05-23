from models.player import Player


def get_first_peers(tournament):
    """
        Récupération des premières paires de joueurs
    """

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
    """
        Récupération des scores des joueurs à un instant T du tournoi
    """

    round_index = 0
    list_players = []

    # On parcours tous les tours du tournoi
    while round_index < len(rounds):
        match_number = 0
        # Pour chaque round, on récupère tous les matchs avec l'identifiant et le score des joueurs
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
            # On cumule les points de chacun des joueurs, à travers tout les matchs de chacun des tours
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
            # Au premier tour, on initialise les dictionnaires avec les nouveaux joueurs rencontrés
            if player_found is False and round_index == 0:
                list_players.append({'player_id': player1_id, 'score': player1_score, 'ranking': player1_ranking})
                list_players.append({'player_id': player2_id, 'score': player2_score, 'ranking': player2_ranking})
            match_number += 1
        round_index += 1

    return list_players


def get_last_peers(list_players, rounds):
    """
        On termine la constitution des paires de joueurs,
        en vérifiant si les joueurs ne se sont pas déjà rencontrés,
        et en modifiant les paires pré-constituées si nécessaire
    """

    new_list_players = []
    list_matchs = []
    i = 0

    # On récupère les paires de joueurs de tous les matchs terminés
    for round in rounds:
        match_number = 0
        while match_number < 4:
            player1_id = round.matchs[match_number][0][0]
            player2_id = round.matchs[match_number][1][0]
            match = [player1_id, player2_id]
            match_miror = [player2_id, player1_id]
            list_matchs.append(match)
            list_matchs.append(match_miror)
            match_number += 1

    # On parcours les paires de joueurs pré-constituées
    while i < 7:
        player1_id = list_players[i]['player_id']
        player1_score = list_players[i]['score']
        player1_ranking = list_players[i]['ranking']
        player2_id = list_players[i + 1]['player_id']
        player2_score = list_players[i + 1]['score']
        player2_ranking = list_players[i + 1]['ranking']
        player1 = {'player_id': player1_id, 'score': player1_score, 'ranking': player1_ranking}
        player2 = {'player_id': player2_id, 'score': player2_score, 'ranking': player2_ranking}
        match = [player1, player2]
        new_list_players.append(player1)
        same_match_found = False
        # On parcours tous les matchs terminés, en vérifiant si la paire courante ne s'est pas déjà rencontrée
        for item_match in list_matchs:
            # Si tel est le cas, on le signale en affectant la valeur True à la variable same_match
            if item_match == match:
                same_match_found = True
                break
        # Si la paire ne s'est jamais croisé, on l'ajoute à la nouvelle liste
        if same_match_found is False:
            new_list_players.append(player2)
        # Dans le cas contraire, on cherche le joueur suivant, et on crée la paire ainsi
        else:
            new_list_players.append(list_players[i + 2]['player_id'])
        i += 2

    return new_list_players


def compare(p1, p2):
    """
        Fonction auxilière, utiliser dans la méthode "sort",
        permettant la constitution des paires de joueurs à partir du second tour
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
