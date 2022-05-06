from core.decorators import controller
from models.player import Player
from models.tournament import Tournament
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
            'player',
            '0',
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
    # On récupère la liste des joueurs du club
    list_players = Player.list()

    # On récupère l'élément de menu choisi par l'utilisateur
    if list_players is not None:
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
        item_menu = PlayerView.print_menu()
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

    if list_tournaments is not None:
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
    # players = []
    tournament = Tournament.read(param)

    if tournament is not None:
        if tournament.step == "1":
            players = tournament.get_tournament_first_ranking()
        else:
            players = tournament.get_other_round_players()

        TournamentView.print_tournament_details(tournament)
        TournamentView.print_tournament_players(players)
        item_menu = TournamentView.print_menu(tournament)
        return item_menu
    else:
        print("Tournoi introuvable")
        return "list_tournaments_controller"


@controller
def play_round_controller(param=None):
    tournament = Tournament.read(param)

    if tournament.step == "1":
        tournament.get_tournament_first_ranking()
        list_round_players = tournament.get_first_round_players()
    elif tournament.step != "finish":
        list_round_players = tournament.get_other_round_players()
    round = PlayRoundView.print_view(list_round_players)
    round['name'] = f"Round{tournament.step}"
    print(round)
    tournament.rounds.append(round)

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


def exit_controller():
    print("A bientôt dans Chess Tournament")
    exit()
