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
from models.player import Player


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
    list_players = Player.list()

    new_player = add_player_view(list_players)
    if new_player is not None:
        obj_player = Player(
            'player',
            '0',
            new_player['firstname'],
            new_player['lastname'],
            new_player['birthday'],
            new_player['sexe'],
            new_player['ranking']
        )
        obj_player.create()
    else:
        print("Annulation de l'ajout")
    return "players_controller"


@controller
def list_players_controller(param=None):
    list_players = Player.list()

    if list_players is not None:
        item_menu = list_players_view(list_players)
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
        item_menu = player_view(player)
        return item_menu


@controller
def tournaments_controller(param=None):
    item_menu = tournaments_view()
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
        new_tournament = add_tournament_view(list_players)
        print(new_tournament)
        return "tournaments_controller"


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


def exit_controller():
    print("A bientôt dans Chess Tournament")
    exit()
