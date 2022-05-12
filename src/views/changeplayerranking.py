from core.decorators import menu
from models.player import Player
from core.validators import is_valid_change_ranking


class ChangePlayerRankingView:
    def print_view(player):
        list_players = Player.list()
        old_player_ranking = player.ranking
        new_player_ranking = ""
        new_list_players = []
        i = 0

        # On trie la liste des joueurs par ordre de classement
        list_players.sort(key=lambda p: int(p.ranking))

        print(f"La position actuelle de {player.firstname} {player.lastname} est {player.ranking}")

        while is_valid_change_ranking(new_player_ranking, list_players) is False:
            new_player_ranking = input("Nouveau classement du joueur : ").strip()

        if new_player_ranking < old_player_ranking:
            for item_player in list_players:
                if new_player_ranking == item_player.ranking:
                    new_list_players.append(player)
                if old_player_ranking == item_player.ranking:
                    continue
                new_list_players.append(item_player)
        elif new_player_ranking > old_player_ranking:
            for item_player in list_players:
                if old_player_ranking == item_player.ranking:
                    continue
                if int(new_player_ranking) + 1 == int(item_player.ranking):
                    new_list_players.append(player)
                new_list_players.append(item_player)
            if int(new_player_ranking) == len(list_players):
                new_list_players.append(player)

        while i < len(new_list_players):
            new_list_players[i].ranking = str(i + 1)
            i += 1

        return new_list_players
