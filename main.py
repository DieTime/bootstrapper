import os
import glob
import sys
from typing import Final, List
from config import Config
from colors import gray, red, green, underline
from getch import getch

DEFAULT_CONFIGS_DIR: Final = 'configs'


def get_config_paths(configs_dir: str) -> List[str]:
    search_query = os.path.join(configs_dir, "**/*.yaml")
    return glob.glob(search_query, recursive=True)


def user_agree(question: str) -> bool:
    message: str = f'{gray("[?]")} {underline(question)}'
    print(f'{message} {gray("y/n")}', end=' ', flush=True)

    answer: str = ''
    while answer not in ['y', 'n']:
        answer = getch().lower()

    agree_str: str = green('Yes') if answer == 'y' else red('No ')
    print(f'\r{message} {agree_str}')

    return answer == 'y'


if __name__ == '__main__':
    configs: List[Config] = []
    accepted_configs: List[Config] = []

    try:
        configs = [Config(cfg_path) for cfg_path in get_config_paths(DEFAULT_CONFIGS_DIR)]
    except RuntimeError as error:
        sys.exit(f'{red("[!]")} {error}')

    accepted_configs = [cfg for cfg in configs if user_agree(cfg.get_question())]
