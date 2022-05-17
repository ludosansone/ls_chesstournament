from core.decorators import controller
from models.player import Player
from models.tournament import Tournament
from models.round import Round
from views.home import HomeView
from views.players import PlayersView
from views.addplayer import AddPlayerView
from views.listplayers import ListPlayersView
from views.player import PlayerView
from views.tournaments import TournamentsView
from views.addtournament import AddTournamentView
from views.listtournaments import ListTournamentsView
from views.tournament import TournamentView
from views.playround import PlayRoundView
from views.generalranking import GeneralRankingView
from views.rounds import RoundsView
from views.changeplayerranking import ChangePlayerRankingView


@controller
def home_controller(param=None):
    item_menu = HomeView.print_menu()
    return item_menu


@controller
def players_controller(param=None):
    item_menu = PlayersView.print_menu()
    return item_menu


@controller
def add_player_controller(param=None):
    list_players = Player.list()

    form_result = AddPlayerView.get_form_result(list_players)

    if form_result is not None:
        player = Player(
            form_result['firstname'],
            form_result['lastname'],
            form_result['birthday'],
            form_result['sexe'],
            form_result['ranking']
        )
        player.create()
    else:
        print("Annulation de l'ajout")
    return "players_controller"


@controller
def list_players_controller(param=None):
    list_players = Player.list()

    if list_players is not None:
        list_players.sort(key=lambda p: p.firstname)
        item_menu = ListPlayersView.print_menu(list_players)
        if item_menu.isdigit() is True:
            return f"player_controller('{item_menu}')"
        else:
            return item_menu
    else:
        print("Aucun joueur enregistré pour le moment")
        return "players_controller"


@controller
def player_controller(param=None):
    player = Player.read(param)

    if player is not None:
        PlayerView.print_view(player)
        item_menu = PlayerView.print_menu(player)
        return item_menu
    else:
        print("Joueur introuvable")
        return "list_players_controller"


@controller
def tournaments_controller(param=None):
    item_menu = TournamentsView.print_menu()
    return item_menu


@controller
def add_tournament_controller(param=None):
    player_number = Player.count()

    if player_number < 8:
        print("Attention : vous avez besoin de 8 joueurs pour créer un tournoi.")
        print(f"Il vous en manque donc {8 - player_number}.")
        print("Nous vous redirigeons vers le formulaire d'ajout de joueur. Revenez en suite créer le tournoi")
        return "add_player_controller"
    else:
        list_players = Player.list()
        form_result = AddTournamentView.get_form_result(list_players)
        form_result['players'].sort()
        tournament = Tournament(
            form_result['name'],
            form_result['place'],
            form_result['dates'],
            form_result['rounds_number'],
            [],
            form_result['players'],
            form_result['time_control'],
            form_result['description']
        )
        tournament.create()
        return f"tournament_controller('{tournament.id}')"


@controller
def list_tournaments_controller(param=None):
    list_tournaments = Tournament.list()

    if list_tournaments != []:
        item_menu = ListTournamentsView.print_menu(list_tournaments)
        if item_menu.isdigit() is True:
            return f"tournament_controller('{item_menu}')"
        else:
            return item_menu
    else:
        print("Aucun tournoi enregistré pour le moment")
        return "tournaments_controller"


@controller
def tournament_controller(param=None):
    tournament = Tournament.read(param)
    players = Player.get_tournament_players(tournament.players)

    if tournament is not None:
        if tournament.step == "1":
            tournament.get_tournament_first_ranking(players)
        elif tournament.step != "finish":
            tournament.get_other_round_players()

        TournamentView.print_tournament_details(tournament)
        TournamentView.print_tournament_players(Player.get_tournament_players(tournament.players), tournament.step)

        item_menu = TournamentView.print_menu(tournament)

        return item_menu
    else:
        print("Tournoi introuvable")
        return "list_tournaments_controller"


@controller
def play_round_controller(param=None):
    tournament = Tournament.read(param)
    players = Player.get_tournament_players(tournament.players)

    if tournament.step == "1":
        tournament.get_tournament_first_ranking(players)
        list_round_players = tournament.get_first_round_players()
        instance_list_players = Player.get_tournament_players(list_round_players)
        for player in instance_list_players:
            tournament.players.append(player.id)
    elif tournament.step != "finish":
        instance_list_players = tournament.get_other_round_players()
    
    dict_round = PlayRoundView.print_view(instance_list_players )
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


@controller
def general_ranking_controller(param=None):
    players = Player.get_general_ranking()
    item_menu = GeneralRankingView.print_menu(players)
    return item_menu


@controller
def rounds_controller(param=None):
    tournament = Tournament.read(param)
    rounds = Round.get_tournament_rounds(tournament.rounds)
    RoundsView.print_rounds(rounds)
    item_menu = RoundsView.print_menu(param)
    return item_menu


@controller
def change_player_ranking_controller(param=None):
    player = Player.read(param)

    new_player_ranking = ChangePlayerRankingView.print_view(player)
    player.change_ranking(new_player_ranking)

    return f"player_controller('{param}')"


def exit_controller():
    print("A bientôt dans Chess Tournament")
    exit()
