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
            ranking=""):

        self.type = type
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.birthday = birthday
        self.sexe = sexe
        self.ranking = ranking

    # Méthodes d'instance
    def create(self):
        db = TinyDB('db.json')
        player_number = Player.count()
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

    # Méthodes de classe
    def read(id):
        db = TinyDB('db.json')
        query = Query()
        results = db.search((query.id == id) & (query.type == "player"))

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

    def count():
        db = TinyDB('db.json')
        query = Query()
        player_number = len(db.search(query.type == 'player'))
        return player_number

    def get_tournament_players(list_id):
        list_player = []

        for id in list_id:
            player = Player.read(id)
            list_player.append(player)
        return list_player

    def get_general_ranking():
        players = Player.list()

        general_ranking = sorted(players, key=lambda p: p.ranking)
        return general_ranking
