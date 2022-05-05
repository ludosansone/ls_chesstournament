from tinydb import TinyDB, Query
from models.player import Player


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

    def read(id):
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

        # On récupère l'ensemble des joueurs participant au tournoi
        players = Player.get_tournament_players(self.players)

        # On trie les joueurs selon leur classement général
        players = sorted(players, key=lambda p: p.ranking)
        return players


    def update_ranking(self):
        step = int(self.step)
        first_ranking = []
        last_ranking = []

        # On met à jour le classement du tournoi selon le total de points des joueurs
        for player in self.players:
            player_found = 0
            dict_player = {'player': player, 'points': 0}
            round_number = 0
            while round_number < step:
                match_number = 0
                while match_number < 4:
                    player_position = 0
                    while player_position < 2:
                        player_id = self.rounds[round_number]['matchs'][match_number][player_position][0]
                        if player_id == player:
                            points = self.rounds[round_number]['matchs'][match_number][player_position][1]
                            dict_player['points'] += float(points)
                            player_found = 1
                        player_position += 1
                    match_number += 1
                if player_found == 1:
                    break
                round_number += 1
            first_ranking.append(dict_player)
        first_ranking.sort(key = lambda r: r['points'], reverse=True)

        # On récupère le classement général des joueurs du tournoi
        general_ranking = self.get_tournament_first_ranking()

        # Si 2 joueurs ont un score égal, on les classe selon leur rang au classement précédent du tournoi
        

        return first_ranking

    def get_other_round_players(self):
        list_players = []
        round_number = int(self.step) - 2
        match_number = 0

        while match_number < 4:
            player1_id = self.rounds[round_number]['matchs'][match_number][0][0]
            player1_score = float(self.rounds[round_number]['matchs'][match_number][0][1])
            player2_id = self.rounds[round_number]['matchs'][match_number][1][0]
            player2_score = float(self.rounds[round_number]['matchs'][match_number][1][1])
            list_players.append({'player_id': player1_id, 'score': player1_score})
            list_players.append({'player_id': player2_id, 'score': player2_score})
            match_number += 1

        # On les trie selon leur nombre de points
        sorted_list_players = sorted(list_players, key=lambda r: r['score'])

        # On crée la liste d'instances à partir de la liste de dictionnaires
        list_players_id = []

        for player in sorted_list_players:
            player_id = player['player_id']
            list_players_id.append(player_id)

        instance_list_players = Player.get_tournament_players(list_players_id)
        return instance_list_players

    # Méthodes de classe
    def list():
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

    def count():
        """
            Comptage du nombre de tournois en base de donéées
        """

        db = TinyDB('db.json')
        query = Query()
        tournament_number = len(db.search(query.type == 'tournament'))
        return tournament_number
