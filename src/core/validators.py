import re


def choice_is_valid(choice, max_index):
    """
        Vérification du choix entrée par l'utilisateur, dans le contexte d'un menu de navigation
    """

    if choice.isdigit() is False:
        return False
    elif (int(choice) - 1) < 0 or (int(choice) - 1) > max_index:
        return False
    else:
        return True


def is_valid_string(str):
    """
        Vérification de la validité d'une chaine de caractère entrée par l'utilisateur
    """

    if str == "":
        return False
    else:
        return True


def is_valid_sexe(str):
    """
        Vérification de la valeur entrée par l'utilisateur, pour le champ "sexe"
    """

    if str == "h" or str == "f" or str == "Homme" or str == "Femme":
        return True
    else:
        return False


def is_valid_date(str):
    """
        Vérification de la valeur entrée par l'utilisateur, pour les champs "begin" et "end"
    """

    if re.match(r"\d{2}/\d{2}/\d{4}", str) is None:
        return False
    else:
        return True


def is_valid_ranking(str, list_players):
    """
        Vérification de la valeur entrée par l'utilisateur, pour le champ "ranking"
        En plus de la vérification du format, on vérifie aussi que la position n'est pas déjà occupée
    """

    if str.isdigit() is True:
        if int(str) > 0:
            if int(str) > (len(list_players) + 1):
                print("Position de classement trop élevée par rapport au nombre de joueurs")
                return False
            else:
                for player in list_players:
                    if int(str) == int(player.ranking):
                        print("Position déjà occupée dans s le classement")
                        return False
            return True
        else:
            return False
    elif str == "":
        return True
    elif str.isdigit() is False:
        return False


def is_valid_change_ranking(str, datas):
    """
        Vérification de la valeur entrée par l'utilisateur, pour le champ "ranking",
        dans le cas d'une modification manuelle du classement
    """

    if str == "" or str.isdigit() is False:
        return False
    elif int(str) > len(datas):
        print("Position de classement trop élevée par rapport au nombre de joueurs")
        return False
    elif int(str) < 0:
        return False
    return True


def is_valid_confirmation(str):
    """
        Vérification de la valeur entrée par l'utilisateur, pour la confirmation d'envoi en base de données
    """

    if str == "o" or str == "n":
        return True
    else:
        return False


def is_valid_player(datas, id):
    """
        Vérification de la validité de l'identifiant du joueur, avant son ajout en base de données
    """

    for data in datas:
        if data.id[0] == id:
            return True
    return False


def is_valid_round_number(round_number):
    """
        Vérification de la validité de l'identifiant du tour, avant son ajout en base de données
    """

    if round_number == "":
        round_number = '4'
    if round_number.isdigit() is True and round_number != '0':
        return True
    else:
        return False


def is_valid_time_control(time_control):
    """
        Vérification de la valeur entrée par l'utilisateur, pour le champ "time_control"
    """

    if time_control == "":
        time_control = '1'
    if time_control.isdigit() is True:
        if int(time_control) > 0 and int(time_control) < 4:
            return True
    return False


def is_valid_score(str):
    """
        Vérification de la valeur entrée par l'utilisateur, pour le champ "score"
    """

    if str == '0' or str == '1' or str == '0.5':
        return True
    else:
        return False
