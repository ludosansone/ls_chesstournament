from core.decorators import controller
from models.player import Player
from views.listplayers import ListPlayersView


@controller
def list_players_controller(param=None):
    list_players = Player.list()

    if list_players is not None:
        list_players.sort(key=lambda p: p.lastname)
        item_menu = ListPlayersView.print_menu(list_players)
        if item_menu.isdigit() is True:
            return f"player_controller('{item_menu}')"
        else:
            return item_menu
    else:
        print("Aucun joueur enregistré pour le moment")
        return "players_controller"
