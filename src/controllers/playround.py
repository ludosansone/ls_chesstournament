from core.decorators import controller
from models.player import Player
from models.tournament import Tournament
from models.round import Round
from views.playround import PlayRoundView


@controller
def play_round_controller(param=None):
    tournament = Tournament.read(param)
    players = Player.get_tournament_players(tournament.players)

    if tournament.step == "1":
        tournament.get_tournament_first_ranking(players)
        tournament.get_first_round_players()
        instance_list_players = Player.get_tournament_players(tournament.players)
    elif tournament.step != "finish":
        instance_list_players = Player.get_tournament_players(tournament.players)

    dict_round = PlayRoundView.print_view(instance_list_players)
    dict_round['name'] = f"Round {tournament.step}"
    instance_round = Round(
        dict_round['name'],
        dict_round['begin'],
        dict_round['end'],
        dict_round['matchs']
    )
    instance_round.create()

    tournament.rounds.append(instance_round.id)

    if tournament.step != "finish":
        if int(tournament.step) < int(tournament.rounds_number):
            new_step = int(tournament.step) + 1
            tournament.step = str(new_step)
        else:
            tournament.step = "finish"

    tournament.update()
    return f"tournament_controller('{param}')"
