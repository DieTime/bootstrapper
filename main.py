import os
import glob
import sys
from typing import Final, List
from config import Config
from termutils import red, user_agree

DEFAULT_CONFIGS_DIR: Final = 'configs'


def get_config_paths(configs_dir: str) -> List[str]:
    search_query = os.path.join(configs_dir, "**/*.yaml")
    return glob.glob(search_query, recursive=True)


if __name__ == '__main__':
    configs: List[Config] = []
    accepted_configs: List[Config] = []

    try:
        configs = [Config(cfg_path) for cfg_path in get_config_paths(DEFAULT_CONFIGS_DIR)]
    except RuntimeError as error:
        sys.exit(f'{red("[!]")} {error}')

    accepted_configs = [cfg for cfg in configs if user_agree(cfg.get_question())]
