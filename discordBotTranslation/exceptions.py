class TranslationException(Exception):
    pass


class DirectoryIsEmpty(TranslationException):
    pass


class AlreadyFormatted(TranslationException):
    pass

class CategoryDoesNotExist(TranslationException):
    pass