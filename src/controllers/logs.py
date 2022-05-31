from core.decorators import controller
from models.tournament import Tournament
from views.logs import LogsView


@controller
def logs_controller(param=None):
    tournament = Tournament.read(param)

    item_menu = LogsView.print_menu(tournament)
    return item_menu
