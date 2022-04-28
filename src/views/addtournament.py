from core.decorators import menu
from core.validators import is_valid_player, is_valid_round_number, is_valid_time_control, is_valid_date


def add_tournament_view(datas=None):
    local_datas = datas
    new_player = None
    i = 0
    name = ""
    place = ""
    players = []
    round_number = ""
    time_control = ""
    begin_date = ""
    end_date = ""
    dates = []
    description = ""

    print("Ajouter un Tournoi\n")

    print("Étape 1 : Nom du Tournoi\n")
    while name == "":
        name = input("Saisissez un nom pour le ttournoi : ").strip()

    print("Étape 2 : Lieu du Tournoi\n")
    while place == "":
        place = input("Saisissez le lieu du ttournoi : ").strip()

    print("Étape 3 : Sélection des joueurs\n")
    while i < 8:
        for data in local_datas:
            if new_player is not None and data.id[0] == new_player:
                local_datas.remove(data)
        for data in local_datas:
            print(f"{data.id[0]} - {data.firstname} {data.lastname}")
        new_player = input(f"Saisissez l'identifiant du joueur {i + 1} : ")
        if is_valid_player(local_datas, new_player) is True:
            players.append(new_player)
            i += 1
        else:
            print(f"{new_player} n'est pas un identifiant valide")

    print("Étape 4 : Configuration du nombre de tours\n")
    while True:
        round_number = input("Saisissez le nombre de tours du tournoi (4 par défaut) : ")
        if is_valid_round_number(round_number) is True:
            break

    print("Étape 5 : Configuration de la gestion du temps\n")
    while True:
        print("1 - Bullet")
        print("2 - Blitz")
        print("3 - Coup rapide")
        time_control = input("Entrez votre choix (Vous pouvez laisser vide pour Bullet)")
        if is_valid_time_control(time_control) is True:
            break

    print("Étape 6 : Configuration des dates\n")
    while True:
        begin_date = input("Saisissez la date de début du tournoi [jj/mm/aaaa] : ")
        if is_valid_date(begin_date) is True:
            dates.append(begin_date)
            break
    while True:
        end_date = input("Saisissez la date de fin [jj/mm/aaaa] (Laissez vide si la date de début est la même) : ")
        if end_date == "":
            end_date = begin_date
        if is_valid_date(end_date) is True:
            dates.append(end_date)
            break

    print("Éttape 7 : Description\n")
    description = input("Vous pouvez saisir une description pour le tournoi (Laissez vide si vous le souhaitez) : ")

    print("Étape 8 : Génération des paires de joueurs\n")

    return {
        'name': name,
        'place': place,
        'players': players,
        'round_number': round_number,
        'time_control': time_control,
        'dates': dates,
        'description': description
    }
