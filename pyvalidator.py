import inspect
from typing import Any, Union


class TypeConvertError(Exception):
    pass


CODE_LIST = {1000: ["ああ", "いい"], 2000: ["abc", "cde"]}


class Field:
    def __init__(self, field_type, code_id: Union[int, None] = None, code_name=False):
        self.field_type = field_type
        self.code_id = code_id
        self.code_name = code_name

    def __set_name__(self, owner, name):
        self.name = name

        if self.code_id is not None:
            self.code__name = name + "__name"

    def _int(self, value: Union[str, int]):
        try:
            return int(value)
        except ValueError:
            TypeConvertError(value)

    def __set__(self, instance, value):
        if self.field_type in [int]:
            value = self._int(value)

        if value in CODE_LIST.keys():
            instance.__dict__[self.name] = value


class AAA(object):
    code_id = Field(int, code_id=1000)
    type_id = Field(str)

    def __new__(cls):
        attributes = inspect.getmembers(cls)

        items = [value for value in attributes if isinstance(value[1], Field)]

        for key, value in items:
            code_id = getattr(value, "code_id")
            if code_id is not None:
                f = Field(str, code_id, code_name=True)
                setattr(cls, key + "__name", f)

        return super().__new__(cls)

    def __init__(self, **kwargs):
        attributes = inspect.getmembers(self)

        items = [value for value in attributes if isinstance(value[1], Field)]

        # for key, value in items:
        #     if getattr(value, "code_id"):
        #         f = Field(str, code_id=getattr(value, "code_id"), code_name=True)
        #         setattr(self, key + "__name", f)

        for key, value in items:
            if key in kwargs.keys():
                setattr(self, key, kwargs[key])
                print(key, value)
            else:
                print("no ", key, value)

    def set_data(self, name, value):
        print(name, value)


f = AAA()
f.code_id = "10"
f.code_id__name = "ああ"

g = AAA()

print(f)
print(f.code_id)

{"name": 1000}
