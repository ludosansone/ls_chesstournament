from core.decorators import menu
from core.transformators import get_smart_date_time


class TournamentRoundsView:
    def print_view(rounds):
        """
            Affichage de la liste de tous les tours d'un trounoi
        """

        print("Liste des tours du tournoi\n")

        for round in rounds:
            print(f"{round.name}")
            print(f"Début : {get_smart_date_time(round.begin)}")
            print(f"Fin :   {get_smart_date_time(round.end)}\n")

    @menu("")
    def print_menu(datas=None):
        """
            Affichage du menu de navigation de la vue
        """

        return [
            {'label': 'Retour aux rapports', 'id': f"logs_controller('{datas.id}')"}
        ]
