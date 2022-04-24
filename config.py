import os
import subprocess
import yaml
from typing import Final, List, Dict
from numbers import Number
from termutils import green, underline, red
from yaspin import yaspin

QUESTION_SECTION: Final = "question"
PRIORITY_SECTION: Final = "priority"
STEPS_SECTION: Final = "steps"

DEFAULT_PRIORITY: Final = 10


class changedir():
    def __init__(self, directory: str):
        self.next_dir = directory
        self.pwd = os.getcwd()

    def __enter__(self):
        os.chdir(self.next_dir)
        return self

    def __exit__(self, type, value, traceback):
        os.chdir(self.pwd)


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
            if self.__data[section] is None:
                raise RuntimeError(f'{underline(path)}: {underline(section)} section is empty')

        if PRIORITY_SECTION not in self.__data:
            self.__data[PRIORITY_SECTION] = DEFAULT_PRIORITY

        if self.__data[PRIORITY_SECTION] is None:
            raise RuntimeError(f'{underline(path)}: {underline(PRIORITY_SECTION)} section is empty')

    def __lt__(self, other) -> bool:
         return self.get_priority() < other.get_priority()

    def get_question(self) -> str:
        return self.__data[QUESTION_SECTION]

    def get_priority(self) -> Number:
        return self.__data[PRIORITY_SECTION]

    def get_steps(self) -> List[Dict[str, List[str]]]:
        return self.__data[STEPS_SECTION]

    def get_name(self) -> str:
        return self.__name

    def get_path(self) -> str:
        return self.__path

    def get_dir(self) -> str:
        return self.__dir

    def process(self):
        err_message = ""

        with changedir(self.get_dir()):
            for step in self.get_steps():
                if err_message != "":
                    break

                description = list(step.keys())[0]
                with yaspin(text=description):
                    for command in step[description]:
                        call = subprocess.run(command, capture_output=True, shell=True)
                        if call.returncode != 0:
                            err_message = call.stderr.decode('utf-8')
                            break

        ok = err_message == ""

        icon = '[!]'
        icon_size = len(icon)

        color = green if ok else red
        color_status = color('Ok' if ok else 'Bad')
        color_icon = color(icon)

        text = self.get_question().replace('?', '')
        print(f'{color_icon} {text} {color_status}')

        if not ok:
            print(f'{" " * icon_size} --> {underline(self.get_path())}')
            print(f'\n{err_message}', end='')
