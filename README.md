<!-- SPDX-License-Identifier: MIT -->

distrans
=======


A simple package to translate your discord bot to different
languages

Key Features
------------

- Fast work and async support.
- The only requirement is [disnake](https://github.com/DisnakeDev/disnake).
- [next-translate](https://github.com/aralroca/next-translate)-like file
  structure and syntax.

Installing
----------

**Python 3.8 or higher is required.**

``` sh
# Linux/macOS
python3 -m pip install -U distrans

# Windows
py -3 -m pip install -U distrans
```

Quick Example
-------------

### Inline translation example

``` py
from distrans import TranslationInteractionBot 

bot = TranslationInteractionBot(
    directory="locales",
    languages=["en", "fr", "es", "uk"]
)

@bot.slash_command()
async def ping(inter, language: str):
    await inter.send(bot.get(
    "common:greeting", 
    code=language, 
    values={"name": inter.user.name}
    )
  )


def main():
    bot.run("TOKEN")

if __name__ == "__main__":
    main()
```

### Using async/await

``` py
translated = await bot.t(
    "common:greeting", 
    code=language, 
    values={"name": inter.user.name}
    )
```

### Advanced usage

``` py
from distrans import TranslationInteractionBot

class MyTranslationInteractionBot(TranslationInteractionBot):
   
    def get_language(**kwargs):
        # kwargs - it's the same kwargs that you're passing to the
        # get() or t() method
        # like:
        # await bot.t("common:greeting", values={"name": "John"}, 
        #inter=inter)
        # you will get an inter object in kwargs
        # Your code here
        return "en" # you can return language code based on current context
        # (guild, user, etc.)

```

#### locales/en/common.json

``` json
{
  "greeting": "Hello, $name!"
}
```

#### locales/fr/common.json

``` json
{
  "greeting": "Bonjour, $name!"
}
```

#### locales/es/common.json

``` json
{
  "greeting": "Hola, $name!"
}
```

#### locales/uk/common.json

``` json
{
  "greeting": "Привіт, $name!"
}
```

