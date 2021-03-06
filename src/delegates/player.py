def move_player_ranking(player, new_player_ranking, list_players):
    """
        Modification de la position d'un joueur dans le classement général
    """

    old_player_ranking = player.ranking
    new_list_players = []

    # Si le joueur doit monter dans le classement
    # on positionne le joueur à la bonne place, et on fait descendre les autres
    if int(new_player_ranking) < int(old_player_ranking):
        for item_player in list_players:
            if new_player_ranking == item_player.ranking:
                new_list_players.append(player)
            if old_player_ranking == item_player.ranking:
                continue
            new_list_players.append(item_player)
    # Si le joueur doit descendre dans le classement
    # on positionne le joueur à la bonne place, et on fait monter les autres
    elif int(new_player_ranking) > int(old_player_ranking):
        for item_player in list_players:
            if old_player_ranking == item_player.ranking:
                continue
            if int(new_player_ranking) + 1 == int(item_player.ranking):
                new_list_players.append(player)
            new_list_players.append(item_player)
        if int(new_player_ranking) == len(list_players):
            new_list_players.append(player)
    return new_list_players
