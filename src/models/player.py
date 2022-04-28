from tinydb import TinyDB, Query


class Player:
    def __init__(
            self,
            type="player",
            id="",
            firstname="",
            lastname="",
            birthday="",
            sexe="",
            ranking=0):

        self.type = type
        self.id = id,
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
            'type': self.type,
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
            result = results[0]
            player = Player(
                result['type'],
                    result['id'],
                    result['firstname'],
                    result['lastname'],
                    result['birthday'],
                    result['sexe'],
                    result['ranking']
            )
            return player
        else:
            return None

    def list():
        db = TinyDB('db.json')
        query = Query()
        results = db.search(query.type == 'player')
        if results is not []:
            list_players = []
            for result in results:
                player = Player(
                    result['type'],
                    result['id'],
                    result['firstname'],
                    result['lastname'],
                    result['birthday'],
                    result['sexe'],
                    result['ranking']
                )
                list_players.append(player)
            return list_players
        else:
            return None
