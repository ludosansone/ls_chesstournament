from core.decorators import controller
from models.tournament import Tournament
from models.round import Round
from views.tournamentmatchs import TournamentMatchsView


@controller
def tournament_matchs_controller(param=None):
    tournament = Tournament.read(param)
    rounds = Round.get_tournament_rounds(tournament.rounds)

    TournamentMatchsView.print_view(rounds)
    item_menu = TournamentMatchsView.print_menu(tournament)
    return item_menu
