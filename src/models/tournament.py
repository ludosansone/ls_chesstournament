from tinydb import TinyDB, Query


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
        self.step = "new"

    # Méthodes d'instances
    def create(self):
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
            'step': 'firstroundready'
        }
        db.insert(document_tournament)

    def read(id):
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

    # Méthodes de classe
    def list():
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
        db = TinyDB('db.json')
        query = Query()
        tournament_number = len(db.search(query.type == 'tournament'))
        return tournament_number
