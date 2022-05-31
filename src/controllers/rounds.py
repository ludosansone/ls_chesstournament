from core.decorators import controller
from models.tournament import Tournament
from models.round import Round
from views.rounds import RoundsView


@controller
def rounds_controller(param=None):
    tournament = Tournament.read(param)
    rounds = Round.get_tournament_rounds(tournament.rounds)
    RoundsView.print_rounds(rounds)
    item_menu = RoundsView.print_menu(param)
    return item_menu
