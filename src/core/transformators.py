def get_smart_time_control(choice):
    """
        Récupération de la valeur intelligible  du contrôle de temps
    """

    choices_dict = {
        '1': 'Bullet',
        '2': 'Blidtz',
        '3': 'Coup rapide'
    }
    return choices_dict[choice]


def get_smart_date_time(date_time):
    """
        Récupération de la date et de l'heure, à un format lisible
    """

    year = date_time[0:4]
    mounth = date_time[5:7]
    day = date_time[8:10]
    houre = date_time[11:13]
    minute = date_time[14:16]
    second = date_time[17:19]

    return f"le {day}/{mounth}/{year} à {houre}:{minute}:{second}"
