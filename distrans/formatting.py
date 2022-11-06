import sys
from string import Template
from discordBotTranslation import AlreadyFormatted


class Formatter:

    def __init__(self, string: str, __values: dict):
        if len(__values.keys()) <= 0:
            raise ValueError("Values cannot be empty")
        self.data = Template(string).safe_substitute(**__values)

    def __str__(self):
        return self.data

    def __repr__(self):
        return self.data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, item):
        return self.data[item]

    def __iter__(self):
        return iter(self.data)

    def __contains__(self, item):
        return item in self.data

    def __add__(self, other):
        return self.data + other

    def __radd__(self, other):
        return other + self.data

    def __mul__(self, other):
        return self.data * other

    def __rmul__(self, other):
        return other * self.data

    def __eq__(self, other):
        return self.data == other

    def __ne__(self, other):
        return self.data != other

    def __lt__(self, other):
        return self.data < other

    def __le__(self, other):
        return self.data <= other

    def __gt__(self, other):
        return self.data > other

    def __ge__(self, other):
        return self.data >= other

    def __hash__(self):
        return hash(self.data)

    def __bool__(self):
        return bool(self.data)

    def __format__(self, format_spec):
        raise AlreadyFormatted("String is already formatted")

    def __dir__(self):
        return dir(self.data)

    def __sizeof__(self):
        return sys.getsizeof(self.data)
