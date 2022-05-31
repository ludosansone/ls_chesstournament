from core.decorators import controller
from models.player import Player
from views.player import PlayerView


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
