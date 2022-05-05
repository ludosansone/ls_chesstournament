import re


def choice_is_valid(choice, max_index):
    if choice.isdigit() is False:
        return False
    elif (int(choice) - 1) < 0 or (int(choice) - 1) > max_index:
        return False
    else:
        return True


def is_valid_string(str):
    if str == "":
        return False
    else:
        return True


def is_valid_sexe(str):
    if str == "h" or str == "f" or str == "Homme" or str == "Femme":
        return True
    else:
        return False


def is_valid_date(str):
    if re.match(r"\d{2}/\d{2}/\d{4}", str) is None:
        return False
    else:
        return True


def is_valid_ranking(str, list_players):
    
    if str.isdigit() is True:
        if int(str) > 0:
            for player in list_players:
                if int(str) == int(player.ranking):
                    print("Position déjà occupée dans s le classement")
                    return False
            return True
        else:
            return False
    elif str == "" or str.isdigit() is False:
        return False


def is_valid_confirmation(str):
    if str == "o" or str == "n":
        return True
    else:
        return False


def is_valid_player(datas, id):
    for data in datas:
        if data.id[0] == id:
            return True
    return False


def is_valid_round_number(round_number):
    if round_number == "":
        round_number = '4'
    if round_number.isdigit() is True and round_number != '0':
        return True
    else:
        return False


def is_valid_time_control(time_control):
    if time_control == "":
        time_control = '1'
    if time_control.isdigit() is True:
        if int(time_control) > 0 and int(time_control) < 4:
            return True
    return False


def is_valid_score(str):
    if str == '0' or str == '1' or str == '0.5':
        return True
    else:
        return False
