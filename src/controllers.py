from core.decorators import controller
from core.example_datas import tournaments_table, players_table
from views.home import home_view
from views.players import players_view
from views.addplayer import add_player_view
from views.listplayers import list_players_view
from views.player import player_view
from views.tournaments import tournaments_view
from views.addtournament import add_tournament_view
from views.listtournaments import list_tournaments_view
from views.tournament import tournament_view


@controller
def home_controller(param=None):
    item_menu = home_view()
    return item_menu


@controller
def players_controller(param=None):
    item_menu = players_view()
    return item_menu


@controller
def add_player_controller(param=None):
    new_player = add_player_view()
    if new_player is not None:
        print("Ajout du joueur en base")
    else:
        print("Annulation de l'ajout")
    return "players_controller"


@controller
def list_players_controller(param=None):
    results = players_table

    item_menu = list_players_view(results)

    if item_menu.isdigit() is True:
        return f"player_controller('{item_menu}')"
    else:
        return item_menu


@controller
def tournaments_controller(param=None):
    item_menu = tournaments_view()
    return item_menu


@controller
def add_tournament_controller(param=None):
    item_menu = add_tournament_view()
    return item_menu


@controller
def list_tournaments_controller(param=None):
    results = tournaments_table

    item_menu = list_tournaments_view(results)

    if item_menu.isdigit() is True:
        return f"tournament_controller('{item_menu}')"
    else:
        return item_menu


@controller
def tournament_controller(param=None):
    results = tournaments_table

    for tournament in results:
        if tournament['id'] == param:
            item_menu = tournament_view(tournament)
            return item_menu
    print("Tournoi introuvable")
    return "list_tournaments_controller"


@controller
def player_controller(param=None):
    results = players_table

    for player in results:
        if player['id'] == param:
            item_menu = player_view(player)
            return item_menu
    print("Joueur introuvable")
    return "list_players_controller"


def exit_controller():
    print("A bientôt dans Chess Tournament")
    exit()
