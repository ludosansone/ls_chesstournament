from core.decorators import controller
from views.home import HomeView


@controller
def home_controller(param=None):
    item_menu = HomeView.print_menu()
    return item_menu
