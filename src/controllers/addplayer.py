from core.decorators import controller
from models.player import Player
from views.addplayer import AddPlayerView


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
