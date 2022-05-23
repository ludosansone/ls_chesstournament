from tinydb import TinyDB, Query


class Round:
    def __init__(
        self,
        name="",
        begin="",
        end="",
        matchs=[]
    ):

        self.id = str(Round.count() + 1)
        self.document_type = "round"
        self.name = name
        self.begin = begin
        self.end = end
        self.matchs = matchs

    # méthodes d'instance
    def create(self):
        """
            Création d'un nouveau tour en base de données
        """

        db = TinyDB('db.json')

        document_round = {
            'id': self.id,
            'document_type': self.document_type,
            'name': self.name,
            'begin': self.begin,
            'end': self.end,
            'matchs': self.matchs
        }
        db.insert(document_round)

    def read(self):
        """
            Récupération du tour en base de données
        """

        db = TinyDB('db.json')
        query = Query()
        results = db.search((query.id == self.id) & (query.document_type == "round"))

        if results is not []:
            result = results[0]
            round = Round(
                result['name'],
                result['begin'],
                result['end'],
                result['matchs'],
            )
            round.document_type = result['document_type']
            round.id = result['id']
            return round
        else:
            return None

    # Méthodes de classe
    @classmethod
    def count(cls):
        """
            Comptage du nombre de tours en base de données
        """

        db = TinyDB('db.json')
        query = Query()
        round_number = len(db.search(query.document_type == 'round'))
        return round_number

    @classmethod
    def get_tournament_rounds(cls, rounds_id):
        """
            Récupération des tours d'un tournoi en base de donnée grace à la liste d'identifiants placée en paramètre
        """

        instance_list_rounds = []
        db = TinyDB('db.json')
        query = Query()

        for id in rounds_id:
            results = db.search((query.id == id) & (query.document_type == "round"))

            result = results[0]
            round = Round(
                result['name'],
                result['begin'],
                result['end'],
                result['matchs'],
            )
            round.document_type = "round"
            round.id = result['id']
            instance_list_rounds.append(round)

        if instance_list_rounds != []:
            return instance_list_rounds
        else:
            return None
