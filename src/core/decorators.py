from core.validators import choice_is_valid
import controllers


def menu(title=""):
    def print_title(function):
        def wrapper(datas=None):
            print(f"{title}\n")

            menu = function(datas)

            menu_max_index = len(menu) - 1

            for item in menu:
                index = menu.index(item)
                print(f"{index + 1} - {item['label']}")

            while True:
                user_choice = input(" Entrez votre choix : ")
                if choice_is_valid(user_choice, menu_max_index):
                    user_choice = int(user_choice)
                    id = menu[user_choice - 1]['id']
                    return id
        return wrapper
    return print_title


def controller(function):
    def wrapper(param=None):
        response = function(param)
        try:
            route = eval("controllers." + response)
            route()
        except AttributeError:
            print("Page introuvable")

    return wrapper
