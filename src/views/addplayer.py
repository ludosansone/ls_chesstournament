from core.validators import is_valid_confirmation, is_valid_date, is_valid_ranking, is_valid_sexe, is_valid_string


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

    while is_valid_ranking(player_ranking, datas) is False:
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
