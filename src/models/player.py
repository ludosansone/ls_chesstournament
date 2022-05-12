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
        """
            création d'un nouveau joueur en base de données
        """

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

        list_players = Player.list()
        old_player_ranking = self.ranking
        new_list_players = []
        i = 0

        # On trie la liste des joueurs par ordre de classement
        list_players.sort(key=lambda p: int(p.ranking))

        # On déplace le joueur dans le classement
        if int(new_player_ranking) < int(old_player_ranking):
            for item_player in list_players:
                if new_player_ranking == item_player.ranking:
                    new_list_players.append(self)
                if old_player_ranking == item_player.ranking:
                    continue
                new_list_players.append(item_player)
        elif int(new_player_ranking) > int(old_player_ranking):
            for item_player in list_players:
                if old_player_ranking == item_player.ranking:
                    continue
                if int(new_player_ranking) + 1 == int(item_player.ranking):
                    new_list_players.append(self)
                new_list_players.append(item_player)
            if int(new_player_ranking) == len(list_players):
                new_list_players.append(self)

        # On réordonne l'ensemble du classement
        while i < len(new_list_players):
            new_list_players[i].ranking = str(i + 1)
            i += 1

        # On met à jour le classement en base de données
        for item_player in new_list_players:
            item_player.update()

    # Méthodes de classe
    def read(id):
        """
            Récupération du joueur en base de donnée, dont l'identifiant est placé en paramètre
        """

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
        """
            Comptage du nombre de joueurs en base de donées
        """

        db = TinyDB('db.json')
        query = Query()
        player_number = len(db.search(query.type == 'player'))
        return player_number

    def get_tournament_players(list_id):
        """
            Récupération des joueurs d'un tournoi, grace à la liste d'identifiants placée en paramètre
        """

        list_player = []

        for id in list_id:
            player = Player.read(id)
            list_player.append(player)
        return list_player

    def get_general_ranking():
        """
            Classement général des joueurs du club
        """

        players = Player.list()

        general_ranking = sorted(players, key=lambda p: p.ranking)
        return general_ranking
