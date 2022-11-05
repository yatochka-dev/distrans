import abc
import json
import os
from abc import ABC
from typing import Any

from .exceptions import DirectoryIsEmpty
from .formatting import Formatter
from .type import language


class AbstractTRBot(ABC):
    @abc.abstractmethod
    def _load_and_compile(self, *args, **kwargs) -> Any:
        raise NotImplementedError

    @abc.abstractmethod
    def _check_directory_exists(self, *args, **kwargs) -> Any:
        raise NotImplementedError

class BaseTranslationBot(AbstractTRBot):
    TRANSLATION_FILE_EXTENSION = ".json"
    BASE_ENCODING = "UTF-8"

    def __init__(self, directory: str, languages: list[language]):
        self._directory = directory
        self._languages = languages

        if len(self._languages) < 2:
            raise ValueError("Language list must contain more than 1 language")

        self._compiled: dict = self._load_and_compile()

    @property
    def compiled(self):
        return self._compiled

    def get_language(self) -> language:
        return self._languages[0]

    def _check_directory_exists(self) -> str:
        if not os.path.exists(self._directory):
            raise FileNotFoundError(
                f"Directory `{self._directory}` does not exist"
            )
        return self._directory

    def _load_and_compile(self) -> dict:
        directory = self._check_directory_exists()
        lang_dirs = os.listdir(directory)
        print(self._languages)
        languages = {}

        if not lang_dirs:
            raise DirectoryIsEmpty(f"Directory `{directory}` is empty")

        for lang_dir in lang_dirs:
            print("lang_dir", lang_dir)
            lang_dir_path = os.path.join(directory, lang_dir)
            if not os.path.isdir(lang_dir_path):
                continue
            if lang_dir not in self._languages:
                print("Language `{lang_dir}` is not in languages list")
                continue

            files = os.listdir(lang_dir_path)
            for file in files:
                file_path = os.path.join(lang_dir_path, file)
                if not os.path.isfile(file_path):
                    continue
                if not file.endswith(self.TRANSLATION_FILE_EXTENSION):
                    continue
                with open(file_path, "r", encoding=self.BASE_ENCODING) as f:
                    data = json.load(f)

                    languages.setdefault(lang_dir, {})

                    languages[lang_dir].setdefault(file.split(".")[0], data)

        return languages

        # files = os.listdir(directory)
        # if 1 > len(files):
        #     raise DirectoryIsEmpty(f"Directory `{directory}` is empty")
        #
        # for file in files:
        #     ext = os.path.splitext(file)[1]
        #     if ext != self.TRANSLATION_FILE_EXTENSION:
        #         continue
        #     with open(os.path.join(directory, file), "r") as f:
        #         yield json.load(f)

    def get(
        self, __key: str, /, values: dict = dict, code: str = None
    ) -> str | Formatter:
        """
        :param __key: file:key pair, example: "common:greeting"
        :param code: language code, example: "en"
        :param values: values to replace in translation
        :return: string
        """

        if not code:
            code = self.get_language()

        if code not in self._languages:
            raise ValueError(f"Language `{code}` is not in languages list")

        file, key = __key.split(":")

        if file not in self.compiled[code]:
            raise KeyError(f"Category `{file}` does not exist")

        if len(values.keys()) > 0:
            return Formatter(
                self.compiled.get(code).get(file).get(key, __key),
                values,
            )

        return self.compiled.get(code).get(file).get(key, __key)

        # class BaseTranslationBot(ABC):
#     TRANSLATION_FILE_EXTENSION = '.json'
#
#     @abc.abstractmethod
#     def load_files(self, *args, **kwargs) -> Any:
#         raise NotImplementedError
#
#     @abc.abstractmethod
#     def compile_files(self, *args, **kwargs) -> Any:
#         raise NotImplementedError
#
#
# class TranslationBot(BaseTranslationBot):
#
#     def __init__(
#             self,
#             *,
#             directory: str,
#     ):
#         self._directory = self._check_directory_exists(directory)
#         self.translated = {
#
#         }
#
#     @staticmethod
#     def _check_directory_exists(directory: str) -> str:
#         if not os.path.exists(directory):
#             raise FileNotFoundError(f'Directory `{directory}` does not exist')
#         return directory
#
#     def load_files(self, directory: str) -> Generator[dict, None, None]:
#
#         files = os.listdir(directory)
#         if 1 > len(files):
#             raise DirectoryIsEmpty(f'Directory `{directory}` is empty')
#
#         for file in files:
#             ext = os.path.splitext(file)[1]
#             if ext != self.TRANSLATION_FILE_EXTENSION:
#                 continue
#             with open(os.path.join(directory, file), 'r') as f:
#                 yield json.load(f)
#
#     def compile_files(self, directory: str) -> dict:
#         compiled = {}
#         for file in self.load_files(directory):
#             compiled.update(file)
#
#         for key, value in compiled.items():
#             if not isinstance(value, str):
#                 raise TypeError(f'Value `{value}` is not a string')
#
#         return compiled
#
#     def assign_translations(self):
#         data = self.compile_files(self._directory)
#
#         for key, value in data.items():
#             setattr(self, key, value)
