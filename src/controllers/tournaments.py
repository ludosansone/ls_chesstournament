from core.decorators import controller
from views.tournaments import TournamentsView


@controller
def tournaments_controller(param=None):
    item_menu = TournamentsView.print_menu()
    return item_menu
