from core.decorators import controller
from models.player import Player
from views.generalranking import GeneralRankingView


@controller
def general_ranking_controller(param=None):
    players = Player.get_general_ranking()
    item_menu = GeneralRankingView.print_menu(players)
    return item_menu
