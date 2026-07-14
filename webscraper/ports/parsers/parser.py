from typing import Generic, TypeVar
from abc import ABC, abstractmethod

T = TypeVar(name="T")


class Parser(ABC, Generic[T]):
    @abstractmethod
    def parse(self, html: str) -> list[T]:
        raise NotImplementedError
