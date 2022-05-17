from functools import cmp_to_key
from tinydb import TinyDB, Query
from models.player import Player
from models.round import Round
from delegates.tournament import get_first_peers, get_all_scores, compare


class Tournament:
    def __init__(
            self,
            name="",
            place="",
            dates=[],
            rounds_number="",
            rounds=[],
            players=[],
            time_control="",
            description=""):

        self.type = "tournament"
        self.id = str(Tournament.count() + 1)
        self.name = name
        self.place = place
        self.dates = dates
        self.rounds_number, = rounds_number,
        self.rounds = rounds
        self.players = players
        self.time_control = time_control
        self.description = description
        self.step = "0"

    # Méthodes d'instances
    def create(self):
        """
            Création d'un nouveau tournoi en base de donnée
        """

        db = TinyDB('db.json')

        document_tournament = {
            'type': self.type,
            'id': self.id,
            'name': self.name,
            'place': self.place,
            'dates': self.dates,
            'rounds_number': self.rounds_number,
            'rounds': self.rounds,
            'players': self.players,
            'time_control': self.time_control,
            'description': self.description,
            'step': '1'
        }
        db.insert(document_tournament)

    def update(self):
        """
            Actualisation du tournoi en base de donnée
        """

        db = TinyDB('db.json')
        query = Query()

        db.update({
            'name': self.name,
            'place': self.place,
            'dates': self.dates,
            'rounds_number': self.rounds_number,
            'rounds': self.rounds,
            'players': self.players,
            'time_control': self.time_control,
            'description': self.description,
            'step': self.step,
        }, (query.id == self.id) & (query.type == "tournament"))

    def get_tournament_first_ranking(self):
        """
            Classement des joueurs pour le premier round du tournoi, en fonction de leur position au classement général
        """

        # On récupère l'ensemble des instances des joueurs participant au tournoi
        instance_list_players = Player.get_tournament_players(self.players)

        # On trie les joueurs selon leur classement général
        instance_list_players.sort(key=lambda p: p.ranking)

        # On réorganise la liste des joueurs du tournoi, en fonction du classement général
        self.players = []

        for player in instance_list_players:
            self.players.append(player.id)

        return instance_list_players

    def get_first_round_players(self):
        """
            consttitution des paires de joueurs pour le premier tour du tournoi
        """

        # On récupère la liste des dictionnaires de joueurs, ordonnée pour le premier tour
        first_round_players = get_first_peers(self)

        # On récupère la liste des instances de joueurs, à partir de la liste de dictionnaires récupérée ci-dessus
        instance_first_round_players = Player.get_tournament_players(first_round_players)

        # On réorganise la liste des joueurs du tournoi, en fonction des paires de joueurs constituées
        self.players = []

        for player in instance_first_round_players:
            self.players.append(player.id)

        return instance_first_round_players

    def get_other_round_players(self):
        """
            constitution des paires de joueurs pour les autres rounds du tournoi
        """

        # On récupère les tours du tournoi
        rounds = Round.get_tournament_rounds(self.rounds)

        # On récupère les joueurs avec leur score des tours précédents, dans une liste de dictionnaires
        list_players = get_all_scores(rounds)

        # On trie les joueurs selon leur nombre de points, ou selon leur rang en cas d'égalité
        list_players.sort(key=cmp_to_key(compare))

        # On réorganise la liste des joueurs du tournoi, avec les paires nouvellement constituées
        self.players = []

        for player in list_players:
            self.players.append(player['player_id'])

        # On récupère la liste des instances des joueurs, dans l'ordre de la dernière réorganisation
        instance_list_players = Player.get_tournament_players(self.players)

        return instance_list_players

    # Méthodes de class
    @classmethod
    def read(cls, id):
        """
            Récupération du tournoi en base de donnée, dont l'identifiant est placé en paramètre
        """

        db = TinyDB('db.json')
        query = Query()
        results = db.search((query.id == id) & (query.type == "tournament"))

        if results is not []:
            result = results[0]
            tournament = Tournament(
                result['name'],
                result['place'],
                result['dates'],
                result['rounds_number'],
                result['rounds'],
                result['players'],
                result['time_control'],
                result['description']
            )
            tournament.type = result['type']
            tournament.id = result['id']
            tournament.step = result['step']
            return tournament
        else:
            return None

    @classmethod
    def list(cls):
        """
            Récupération de la liste de l'ensemble des tournois
        """

        db = TinyDB('db.json')
        query = Query()
        results = db.search(query.type == 'tournament')
        if results is not []:
            list_tournaments = []
            for result in results:
                tournament = Tournament(
                    result['name'],
                    result['place'],
                    result['dates'],
                    result['rounds_number'],
                    result['rounds'],
                    result['players'],
                    result['time_control'],
                    result['description'],
                )
                tournament.type = result['type']
                tournament.id = result['id']
                tournament.step = result['step']
                list_tournaments.append(tournament)
            return list_tournaments
        else:
            return None

    @classmethod
    def count(cls):
        """
            Comptage du nombre de tournois en base de donées
        """

        db = TinyDB('db.json')
        query = Query()
        tournament_number = len(db.search(query.type == 'tournament'))
        return tournament_number
