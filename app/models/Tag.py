class Tag:

    def __init__(self, name_tag: str):
        self.__name_tag = name_tag

    @property
    def name_tag(self) -> str:
        return self.__name_tag

    @name_tag.setter
    def name_tag(self, value):
        if not isinstance(value, str):
            raise TypeError("name_tag must be a string")

        self.__name_tag = value.strip().lower()
