from core.decorators import controller
from models.player import Player
from models.tournament import Tournament
from views.playersalphabeticorder import PlayersAlphabeticOrderView


@controller
def players_alphabetic_order_controller(param=None):
    tournament = Tournament.read(param)
    list_players = Player.get_tournament_players(tournament.players)

    list_players.sort(key=lambda p: p.lastname)

    PlayersAlphabeticOrderView.print_view(list_players)
    item_menu = PlayersAlphabeticOrderView.print_menu(tournament)
    return item_menu
