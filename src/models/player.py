from tinydb import TinyDB, Query


class Player:
    def __init__(
            self,
            firstname="",
            lastname="",
            birthday="",
            sexe="",
            ranking=0):

        self.firstname = firstname
        self.lastname = lastname
        self.birthday = birthday
        self.sexe = sexe
        self.ranking = ranking

    def create(self):
        db = TinyDB('db.json')
        query = Query()
        player_number = len(db.search(query.type == 'player'))
        new_id = str(player_number + 1)

        document_player = {
            'type': 'player',
            'id': new_id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'birthday': self.birthday,
            'sexe': self.sexe,
            'ranking': self.ranking
        }
        db.insert(document_player)

    def read(id):
        db = TinyDB('db.json')
        query = Query()
        results = db.search(query.id == id)

        if results is not []:
            return results[0]
        else:
            return None

    def list():
        db = TinyDB('db.json')
        query = Query()
        results = db.search(query.type == 'player')
        if results is not []:
            return results
        else:
            return None
