from core.decorators import controller
from models.tournament import Tournament
from views.listtournaments import ListTournamentsView


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
