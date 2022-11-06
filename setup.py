from pkg_resources import parse_requirements
from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()


setup(
    name="discordBot-translation-Philip Sagan",
    version="0.0.1",
    author="Philip Sagan",
    author_email="philipchef13@gmail.com",
    description="Package to translate your discord bots",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yatochka-dev/discordBot-translation",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "disnake>=2.*.*"
    ]
)
