from disnake import Client, AutoShardedClient
from disnake.ext.commands import (
    Bot,
    AutoShardedBot,
    InteractionBot,
    AutoShardedInteractionBot,
    BotBase,
)

from .type import language
from .main import BaseTranslationBot

__all__ = [
    "TranslationClient",
    "TranslationAutoShardedClient",
    "TranslationBot",
    "TranslationAutoShardedBot",
    "TranslationInteractionBot",
    "TranslationAutoShardedInteractionBot",
    "TranslationBotBase"
]


class TranslationClient(Client, BaseTranslationBot):
    def __init__(
            self,
            directory: str,
            languages: list[language],
            **kwargs,
    ):
        super().__init__(**kwargs)
        BaseTranslationBot.__init__(
            self, directory=directory, languages=languages
        )


class TranslationAutoShardedClient(AutoShardedClient, BaseTranslationBot):
    def __init__(
            self,
            directory: str,
            languages: list[language],
            **kwargs,
    ):
        super().__init__(**kwargs)
        BaseTranslationBot.__init__(
            self, directory=directory, languages=languages
        )


class TranslationBot(Bot, BaseTranslationBot):
    def __init__(
            self,
            directory: str,
            languages: list[language],
            **kwargs,
    ):
        super().__init__(**kwargs)
        BaseTranslationBot.__init__(
            self, directory=directory, languages=languages
        )


class TranslationAutoShardedBot(AutoShardedBot, BaseTranslationBot):
    def __init__(
            self,
            directory: str,
            languages: list[language],
            **kwargs,
    ):
        super().__init__(**kwargs)
        BaseTranslationBot.__init__(
            self, directory=directory, languages=languages
        )


class TranslationInteractionBot(InteractionBot, BaseTranslationBot):
    def __init__(
            self,
            directory: str,
            languages: list[language],
            **kwargs,
    ):
        super().__init__(**kwargs)
        BaseTranslationBot.__init__(
            self, directory=directory, languages=languages
        )


class TranslationAutoShardedInteractionBot(
    AutoShardedInteractionBot, BaseTranslationBot
):
    def __init__(
            self,
            directory: str,
            languages: list[language],
            **kwargs,
    ):
        super().__init__(**kwargs)
        BaseTranslationBot.__init__(
            self, directory=directory, languages=languages
        )


class TranslationBotBase(BotBase, BaseTranslationBot):
    def __init__(
            self,
            directory: str,
            languages: list[language],
            **kwargs,
    ):
        super().__init__(**kwargs)
        BaseTranslationBot.__init__(
            self, directory=directory, languages=languages
        )
