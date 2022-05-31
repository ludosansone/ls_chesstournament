from controllers.home import home_controller


# Point d'entrée du programme
if __name__ == '__main__':
    try:
        home_controller()
    except KeyboardInterrupt:
        print("\nA bientôt dans Chess Tournament")
