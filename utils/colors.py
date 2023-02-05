from colorama import Fore


def r_color(text):
    '''Красный цвет'''
    text = Fore.RED + text + Fore.RESET
    return text


def y_color(text):
    '''Желтый цвет'''
    text = Fore.YELLOW + text + Fore.RESET
    return text


def g_color(text):
    '''Зеленый цвет'''
    text = Fore.GREEN + text + Fore.RESET
    return text
