from core.decorators import menu
from models.player import Player
from core.validators import is_valid_change_ranking


class ChangePlayerRankingView:
    def print_view(player):
        """
            Modification de la position d'un joueur dans le classement général
        """

        list_players = Player.list()
        new_player_ranking = ""

        print(f"La position actuelle de {player.firstname} {player.lastname} est {player.ranking}")

        while is_valid_change_ranking(new_player_ranking, list_players) is False:
            new_player_ranking = input("Nouveau classement du joueur : ").strip()

        return new_player_ranking
