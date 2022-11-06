from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

VERSION = "0.0.1"
DESCRIPTION = "A simple translation library for discord bots"

setup(
    name="distrans",
    version=VERSION,
    author="Philip Sagan/Yatochka",
    author_email="philipchef13@gmail.com",
    description=DESCRIPTION,
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
        "disnake"
    ]
)
