from tinydb import TinyDB, Query


class Round:
    def __init__(
            self,
            name="",
            matchs=[]):
        self.type = "round"
        self.id = str(Round.count() + 1)
        self.name = name
        self.matchs = matchs

    # Méthodes d'instance
    def create(self):
        db = TinyDB('db.json')

        document_round = {
            'type': self.type,
            'id': self.id,
            'match': self.match,
        }
        db.insert(document_round)

    # Méthodes de classe
    def count():
        db = TinyDB('db.json')
        query = Query()
        round_number = len(db.search(query.type == 'round'))
        return round_number
