from controllers import home_controller


if __name__ == '__main__':
    try:
        home_controller()
    except KeyboardInterrupt:
        print("\nA bientôt dans Chess Tournament")
