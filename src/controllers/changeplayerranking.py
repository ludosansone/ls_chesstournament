from core.decorators import controller
from models.player import Player
from views.changeplayerranking import ChangePlayerRankingView


@controller
def change_player_ranking_controller(param=None):
    player = Player.read(param)

    new_player_ranking = ChangePlayerRankingView.print_view(player)
    player.change_ranking(new_player_ranking)

    return f"player_controller('{param}')"
