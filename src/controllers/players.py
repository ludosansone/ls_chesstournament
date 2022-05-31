from core.decorators import controller
from views.players import PlayersView


@controller
def players_controller(param=None):
    item_menu = PlayersView.print_menu()
    return item_menu
