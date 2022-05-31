from core.decorators import controller
from models.player import Player
from models.tournament import Tournament
from views.playersrankingorder import PlayersRankingOrderView


@controller
def players_ranking_order_controller(param=None):
    tournament = Tournament.read(param)
    list_players = Player.get_tournament_players(tournament.players)

    PlayersRankingOrderView.print_view(list_players)
    item_menu = PlayersRankingOrderView.print_menu(tournament)
    return item_menu
