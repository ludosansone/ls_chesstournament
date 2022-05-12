from core.decorators import menu
from models.player import Player
from core.validators import is_valid_ranking


class ChangePlayerRankingView:
    def print_view(player):
        list_players = Player.list()
        player_ranking = ""

        print(f"La position actuelle de {player.firstname} {player.lastname} est {player.ranking}")

        player_ranking = input("Nouvelle poosition du joueur dans le Classement : ").strip()



