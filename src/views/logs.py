from core.decorators import menu


class LogsView:
    @menu("Rapports")
    def print_menu(datas=None):
        """
            Affichage de la liste des rapports propres à un tournoi
        """

        return [
            {
                'label': 'Joueurs du tournoi par ordre alphabétique',
                'id': f"players_alphabetic_order_controller('{datas.id}')"
            },
            {
                'label': 'Joueurs du tournoi par ordre de classement',
                'id': f"players_ranking_order_controller('{datas.id}')"
            },
            {
                'label': 'Tours du tournoi',
                'id': f"tournament_rounds_controller('{datas.id}')"
            },
            {
                'label': 'Matchs du tournoi',
                'id': f"tournament_matchs_controller('{datas.id}')"
            },
            {
                'label': 'Retour aux détails du tournoi',
                'id': f"tournament_controller('{datas.id}')"
            }
        ]
