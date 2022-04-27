from core.decorators import menu
from core.validators import is_valid_confirmation, is_valid_date, is_valid_ranking, is_valid_sexe, is_valid_string


@menu("Menu Principal")
def home_view(datas=None):
    return [
        {'label': 'Gestion des Joueurs', 'id': 'players_controller'},
        {'label': 'Gestion des Tournois', 'id': 'tournaments_controller'},
        {'label': 'Quitter le programme', 'id': 'exit_controller'},
    ]


@menu("Gestion des Joueurs")
def players_view(datas=None):
    return [
        {'label': 'Ajouter un Joueur', 'id': 'add_player_controller'},
        {'label': 'lister les Joueurs', 'id': 'list_players_controller'},
        {'label': 'Retourner au menu principal', 'id': 'home_controller'},
    ]


def add_player_view(datas=None):
    player_firstname = ""
    player_lastname = ""
    player_sexe = ""
    player_birthday = ""
    player_ranking = "unknown"
    user_confirmation = "unknown"

    while is_valid_string(player_firstname) is False:
        player_firstname = input("Prénom du joueur : ").strip()

    while is_valid_string(player_lastname) is False:
        player_lastname = input("Nom du joueur : ").strip()

    while is_valid_sexe(player_sexe) is False:
        player_sexe = input("Est-ce un home ou une femme [h/f] : ").strip()
        if player_sexe == "f":
            player_sexe = "Femme"
        else:
            player_sexe = "Homme"

    while is_valid_date(player_birthday) is False:
        player_birthday = input("Date d'anniversaire du joueur [jj/mm/aaaa] : ").strip()

    while is_valid_ranking(player_ranking) is False:
        player_ranking = input("Classement du joueur (Laissez vide pour non-classé : )").strip()
        if player_ranking == "":
            player_ranking = "non-classé"

    print("\nRésumé\n")

    print(f"{player_firstname} {player_lastname}")
    print(f"{player_sexe}")
    print(f"Né le {player_birthday}")
    print(f"Classement : {player_ranking}")

    while is_valid_confirmation(user_confirmation) is False:
        user_confirmation = input("Souhaitez-vous confirmer (Laissez vide pour dire oui) ? [o/n] : ").strip()
        if user_confirmation == "o" or user_confirmation == "":
            return {
                'firstname': player_firstname,
                'lastname': player_lastname,
                'sexe': player_sexe,
                'birthday': player_birthday,
                'ranking': player_ranking,
            }
        else:
            return None


@menu("Liste des Joueurs")
def list_players_view(datas=None):
    menu = []

    if datas != []:
        for player in datas:
            new_item_menu = {'label': f"{player['firstname']} {player['lastname']}", 'id': player['id']}
            menu.append(new_item_menu)
    else:
        print("Aucun joueur enregistré\n")
        menu.append({'label': 'Ajouter un joueur', 'id': 'add_player_controller'})

    menu.append({'label': 'Retour à la gestion des joueurs', 'id': 'players_controller'})

    return menu


@menu("Détail du Joueur")
def player_view(datas=None):
    print(f"{datas['firstname']} {datas['lastname']} ({datas['sexe']})")
    print(f"né le {datas['birthday']}")
    print(f"Classement : {datas['ranking']}\n")

    return [
        {'label': 'Retour à la liste des joueurs', 'id': 'list_players_controller'},
        {'label': 'Retour à la gestion des joueurs', 'id': 'players_controller'},
    ]


@menu("Gestion des Tournois")
def tournaments_view(datas=None):
    return [
        {'label': 'Ajouter un Tournoi', 'id': 'add_tournament_controller'},
        {'label': 'lister les Tournois', 'id': 'list_tournaments_controller'},
        {'label': 'Retourner au menu principal', 'id': 'home_controller'},
    ]


@menu("Ajouter un Tournoi")
def add_tournament_view(datas=None):
    print("Ici, le formulaire d'ajout d'un tournoi")
    return [
        {'label': 'Retour à la gestion des tournois', 'id': 'tournaments_controller'}
    ]


@menu("Liste des Tournois")
def list_tournaments_view(datas=None):
    menu = []
    if datas != []:
        for tournament in datas:
            new_item_menu = {'label': tournament['name'], 'id': tournament['id']}
            menu.append(new_item_menu)
    else:
        print("Aucun tournoi enregistré\n")
        menu.append({'label': 'Ajouter un tournoi', 'id': 'add_tournament_controller'})

    menu.append({'label': 'Retour à la gestion des tournois', 'id': 'tournaments_controller'})

    return menu


@menu("Détail du tournoi")
def tournament_view(datas=None):
    print(f"Nom du tournoi : {datas['name']}")

    print(f"Lieu : {datas['place']}")

    if datas['dates'][0] == datas['dates'][1]:
        print(f"Le : {datas['dates'][0]}")
    else:
        print(f"Du {datas['dates'][0]} au {datas['dates'][1]}")

    return [
        {'label': 'Retour à la liste des tournois', 'id': 'list_tournaments_controller'},
        {'label': 'Retour à la gestion des tournois', 'id': 'tournaments_controller'},
    ]
