import os
import yaml
from typing import Final

QUESTION_SECTION: Final = "question"
STEPS_SECTION: Final = "steps"


class Config:
    def __init__(self, path: str):
        self.__path: str = path
        self.__name: str = os.path.basename(path)

        with open(path, 'r') as config:
            try:
                self.__data: dict[str, any] = yaml.load(config, Loader=yaml.SafeLoader)
            except SyntaxError:
                raise RuntimeError(f'Invalid "{path}" config file: invalid syntax')

        for section in [QUESTION_SECTION, STEPS_SECTION]:
            if section not in self.__data:
                raise RuntimeError(f'Invalid "{path}" config file: {section} section not found')

    def get_question(self):
        return self.__data[QUESTION_SECTION]

    def get_steps(self):
        return self.__data[STEPS_SECTION]

    def get_name(self):
        return self.__name

    def get_path(self):
        return self.__path
