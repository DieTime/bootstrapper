import os
import glob
import sys
from typing import Final, List
from config import Config
from colors import gray, red, green, underline
from getch import getch

DEFAULT_CONFIGS_DIR: Final = 'configs'


def get_yaml_config_paths(configs_dir: str) -> List[str]:
    yaml_config_paths: List[str] = []

    for directory, _, _ in os.walk(configs_dir):
        dir_yaml_config_paths: List[str] = glob.glob(os.path.join(f'{directory}/*.yaml'))
        yaml_config_paths.extend(dir_yaml_config_paths)

    return yaml_config_paths


def user_agree(question: str) -> bool:
    message: str = gray("[?]") + " " + underline(question)
    helper: str = gray("y/n")

    print(f'{message} {helper}', end=' ', flush=True)

    answer: str = ''
    while answer not in ['y', 'n']:
        answer = getch().lower()

    agree: bool = answer == 'y'
    agree_str: str = green('Yes') if agree else red('No ')

    print(f'\r{message} {agree_str}')
    return agree


if __name__ == '__main__':
    configs: List[Config] = []
    accepted_configs: List[Config] = []

    try:
        for yaml_config_path in get_yaml_config_paths(DEFAULT_CONFIGS_DIR):
            configs.append(Config(yaml_config_path))
    except (RuntimeError, FileNotFoundError) as err:
        sys.exit(f'{red("[!]")} {err}')

    for config in configs:
        if user_agree(config.get_question()):
            accepted_configs.append(config)

    print(accepted_configs)
