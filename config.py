import os
import yaml
from typing import Final, List
from colors import underline

QUESTION_SECTION: Final = "question"
STEPS_SECTION: Final = "steps"


class Config:
    def __init__(self, path: str):
        self.__path: str = path
        self.__name: str = os.path.basename(path)
        self.__dir: str = os.path.dirname(path)

        if not os.path.exists(self.__path):
            raise RuntimeError(f'{underline(path)}: file {underline("not exists")}')

        with open(path, 'r') as config:
            try:
                self.__data: dict[str, any] = yaml.load(config, Loader=yaml.SafeLoader)
            except SyntaxError:
                raise RuntimeError(f'{underline(path)}: invalid {underline("syntax")}')

        for section in [QUESTION_SECTION, STEPS_SECTION]:
            if section not in self.__data:
                raise RuntimeError(f'{underline(path)}: {underline(section)} section not found')

    def get_question(self) -> str:
        return self.__data[QUESTION_SECTION]

    def get_steps(self) -> List[List[str]]:
        return self.__data[STEPS_SECTION]

    def get_name(self) -> str:
        return self.__name

    def get_path(self) -> str:
        return self.__path

    def get_dir(self) -> str:
        return self.__dir
