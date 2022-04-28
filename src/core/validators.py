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


def is_valid_ranking(str):
    if str.isdigit() is True:
        if int(str) > 0:
            return True
    elif str == "" or str == "non-classé":
        return True
    else:
        return False


def is_valid_confirmation(str):
    if str == "o" or str == "n":
        return True
    else:
        return False
