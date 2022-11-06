import abc
import json
import os
from abc import ABC
from typing import Any

from asgiref.sync import sync_to_async

from .exceptions import DirectoryIsEmpty, CategoryDoesNotExist
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
        self.languages = languages

        if len(self.languages) < 2:
            raise ValueError("Language list must contain more than 1 language")

        self._compiled: dict = self._load_and_compile()

    def get_language(self, **kwargs) -> language:

        """
        :param kwargs: kwargs to pass to get_language method from self.get
        method
        :return: language code, code should be in self.languages
        """

        return self.languages[0]

    def get(
        self, __key: str, /, values: dict = dict, code: str = None, **kwargs
    ) -> str | Formatter:

        """
        :param __key: file:key pair, example: "common:greeting"
        :param code: language code, example: "en"
        :param values: values to replace in translation
        :return: string
        """

        if not code:
            code = self.get_language(**kwargs)

        if code not in self.languages:
            raise ValueError(f"Language `{code}` is not in languages list")

        # splits __key into file and key
        # example: "common:greeting" -> ["common", "greeting"]
        file, key = __key.split(":")

        if file not in self.compiled[code]:
            raise CategoryDoesNotExist(f"Category `{file}` does not exist")

        if len(values.keys()) > 0:
            # if values are passed, return Formatter object
            return Formatter(
                self.compiled.get(code).get(file).get(key, __key),
                values,
            )

        # else returns string
        return self.compiled.get(code).get(file).get(key, __key)

        # class BaseTranslationBot(ABC):

    async def t(
        self, __key: str, /, values: dict = dict, code: str = None, **kwargs
    ) -> str | Formatter:
        return await sync_to_async(self.get)(
            __key, values=values, code=code, **kwargs
        )

    def _check_directory_exists(self) -> str:
        if not os.path.exists(self._directory):
            raise FileNotFoundError(
                f"Directory `{self._directory}` does not exist"
            )
        return self._directory

    def _load_and_compile(self) -> dict:
        directory = self._check_directory_exists()
        lang_dirs = os.listdir(directory)
        print(self.languages)
        languages = {}

        if not lang_dirs:
            raise DirectoryIsEmpty(f"Directory `{directory}` is empty")

        for lang_dir in lang_dirs:
            print("lang_dir", lang_dir)
            lang_dir_path = os.path.join(directory, lang_dir)
            if not os.path.isdir(lang_dir_path):
                continue
            if lang_dir not in self.languages:
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

    @property
    def compiled(self):
        return self._compiled
