from typing import Any, TypeAlias

JSON: TypeAlias = dict[str, Any]


class Model:
    def __init__(self, payload: JSON) -> None:
        self.payload = payload


class Field:
    def __init__(self, path: str) -> None:
        self.path = path.split('.')

    def __get__(self, instance: Model, owner: type[Model]) -> Any:
        if instance is None:
            return self
        value = instance.payload
        try:
            for key in self.path:
                value = value.get(key)
                if value is None:
                    break
            return value
        except (AttributeError, TypeError):
            return None

    def __set__(self, instance: Model, value: Any) -> None:
        if instance is None:
            return
        data = instance.payload
        for key in self.path[:-1]:
            if key not in data or not isinstance(data[key], dict):
                data[key] = {}
            data = data[key]
        data[self.path[-1]] = value
