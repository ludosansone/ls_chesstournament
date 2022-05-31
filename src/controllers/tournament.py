from core.decorators import controller
from models.player import Player
from models.tournament import Tournament
from models.round import Round
from views.tournament import TournamentView


@controller
def tournament_controller(param=None):
    tournament = Tournament.read(param)
    players = Player.get_tournament_players(tournament.players)
    rounds = Round.get_tournament_rounds(tournament.rounds)

    if tournament is not None:
        if tournament.step == "1":
            tournament.get_tournament_first_ranking(players)
        elif tournament.step != "finish":
            tournament.get_other_round_players(rounds)

        TournamentView.print_tournament_details(tournament)
        if tournament.step == "1" or tournament.step == "finish":
            TournamentView.print_ranking(Player.get_tournament_players(tournament.players), tournament.step)
        else:
            TournamentView.print_futur_matchs(Player.get_tournament_players(tournament.players))

        item_menu = TournamentView.print_menu(tournament)

        return item_menu
    else:
        print("Tournoi introuvable")
        return "list_tournaments_controller"
