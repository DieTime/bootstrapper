from getch import getch


def underline(text: str) -> str:
    return f'\033[4m{text}\033[0m'


def red(text: str) -> str:
    return f'\033[31m{text}\033[0m'


def green(text: str) -> str:
    return f'\033[32m{text}\033[0m'


def gray(text: str) -> str:
    return f'\033[97m{text}\033[0m'


def user_agree(question: str) -> bool:
    message: str = f'{gray("[?]")} {question}'
    print(f'{message} {gray("y/n")}', end=' ', flush=True)

    answer: str = ''
    while answer not in ['y', 'n']:
        answer = getch().lower()

    agree_str: str = green('Yes') if answer == 'y' else red('No ')
    print(f'\r{message} {agree_str}')

    return answer == 'y'
