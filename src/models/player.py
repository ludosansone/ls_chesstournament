from tinydb import TinyDB, Query
from models.playerdelegate import PlayerDelegate


class Player:
    def __init__(
            self,
            firstname="",
            lastname="",
            birthday="",
            sexe="",
            ranking=""):

        self.type = "player"
        self.id = str(Player.count() + 1)
        self.firstname = firstname
        self.lastname = lastname
        self.birthday = birthday
        self.sexe = sexe
        self.ranking = ranking

    # Méthodes d'instance
    def create(self):
        """
            Création d'un nouveau joueur en base de données
        """

        db = TinyDB('db.json')

        document_player = {
            'type': self.type,
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'birthday': self.birthday,
            'sexe': self.sexe,
            'ranking': self.ranking
        }
        db.insert(document_player)

    def update(self):
        """
            Actualisation du joueuren base de donnée
        """

        db = TinyDB('db.json')
        query = Query()

        db.update({
            'type': self.type,
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'birthday': self.birthday,
            'sexe': self.sexe,
            'ranking': self.ranking
        }, (query.id == self.id) & (query.type == "player"))

    def change_ranking(self, new_player_ranking):
        """
            Changement de la position du joueur dans le classement général
        """

        # On trie la liste des joueurs par ordre de classement
        list_players = Player.list()
        list_players.sort(key=lambda p: int(p.ranking))

        # On déplace le joueur dans le classement, puis on retourne la liste réordonnée
        new_list_players = PlayerDelegate.move_player_ranking(self, new_player_ranking, list_players)

        # On met à jour la propriété ranking de l'ensemble des joueurs
        i = 0
        while i < len(new_list_players):
            new_list_players[i].ranking = str(i + 1)
            i += 1

        # On met à jour le classement en base de données
        for item_player in new_list_players:
            item_player.update()

    # Méthodes de classe
    @classmethod
    def read(cls, id):
        """
            Récupération du joueur en base de donnée, dont l'identifiant est placé en paramètre
        """

        db = TinyDB('db.json')
        query = Query()
        results = db.search((query.id == id) & (query.type == "player"))

        if results is not []:
            result = results[0]
            player = Player(
                result['firstname'],
                result['lastname'],
                result['birthday'],
                result['sexe'],
                result['ranking']
            )
            player.type = result['type']
            player.id = result['id']

            return player
        else:
            return None

    @classmethod
    def list(cls):
        """
            Récupération de la liste de l'ensemble des joueurs
        """

        db = TinyDB('db.json')
        query = Query()
        results = db.search(query.type == 'player')
        if results is not []:
            list_players = []
            for result in results:
                player = Player(
                    result['firstname'],
                    result['lastname'],
                    result['birthday'],
                    result['sexe'],
                    result['ranking']
                )
                player.type = result['type']
                player.id = result['id']
                list_players.append(player)
            return list_players
        else:
            return None

    @classmethod
    def count(cls):
        """
            Comptage du nombre de joueurs en base de donées
        """

        db = TinyDB('db.json')
        query = Query()
        player_number = len(db.search(query.type == 'player'))
        return player_number

    @classmethod
    def get_tournament_players(cls, list_id):
        """
            Récupération des joueurs d'un tournoi, grace à la liste d'identifiants placée en paramètre
        """

        list_player = []

        for id in list_id:
            player = Player.read(id)
            list_player.append(player)
        return list_player

    @classmethod
    def get_general_ranking(cls):
        """
            Classement général des joueurs du club
        """

        players = Player.list()

        # On trie les joueurs en fonction de leur propriété ranking
        general_ranking = sorted(players, key=lambda p: int(p.ranking))
        return general_ranking
