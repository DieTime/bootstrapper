def underline(text: str) -> str:
    return f'\033[4m{text}\033[0m'


def red(text: str) -> str:
    return f'\033[31m{text}\033[0m'


def green(text: str) -> str:
    return f'\033[32m{text}\033[0m'


def gray(text: str) -> str:
    return f'\033[97m{text}\033[0m'
