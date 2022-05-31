from core.decorators import controller
from models.player import Player
from models.tournament import Tournament
from views.addtournament import AddTournamentView


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
