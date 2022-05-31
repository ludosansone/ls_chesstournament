from core.decorators import controller
from models.tournament import Tournament
from models.round import Round
from views.tournamentrounds import TournamentRoundsView


@controller
def tournament_rounds_controller(param=None):
    tournament = Tournament.read(param)
    rounds = Round.get_tournament_rounds(tournament.rounds)

    TournamentRoundsView.print_view(rounds)
    item_menu = TournamentRoundsView.print_menu(tournament)
    return item_menu
