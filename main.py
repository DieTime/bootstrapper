import os
import glob
import sys
import subprocess
from typing import Final, List
from config import Config
from termutils import underline, gray, red, green, user_agree

DEFAULT_CONFIGS_DIR: Final = 'configs'


def get_config_paths(configs_dir: str) -> List[str]:
    search_query = os.path.join(configs_dir, "**/*.yaml")
    return glob.glob(search_query, recursive=True)


def request_sudo_session() -> bool:
    print(f'{gray("[!]")} Please login to {underline("sudo")} session')

    call = subprocess.run(['sudo', 'echo', '-n', '""'], capture_output=True)
    if call.returncode != 0:
        print(f'{red("[!]")} Failed to login to {underline("sudo")} session {red("Bad")}')
        return False

    print(f'{green("[!]")} Successfully login to {underline("sudo")} session {green("Ok")}')
    return True


if __name__ == '__main__':
    configs: List[Config] = []
    accepted_configs: List[Config] = []

    try:
        configs = [Config(cfg_path) for cfg_path in get_config_paths(DEFAULT_CONFIGS_DIR)]
    except RuntimeError as error:
        sys.exit(f'{red("[!]")} {error}')

    configs = sorted(configs)
    accepted_configs = [cfg for cfg in configs if user_agree(cfg.get_question())]

    if not request_sudo_session():
        sys.exit(1)

    print('-------------------------')

    for config in accepted_configs:
        config.process()
