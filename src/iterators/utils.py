from dataclasses import dataclass, field
from itertools import batched
from typing import Any, Iterable, Self, TypeAlias

SomeRemoteData: TypeAlias = int


@dataclass
class Query:
    per_page: int = 3
    page: int = 1


@dataclass
class Page:
    per_page: int = 3
    results: Iterable[SomeRemoteData] = field(default_factory=list)
    next: int | None = None


def request(query: Query) -> Page:
    data = [i for i in range(0, 10)]
    chunks = list(batched(data, query.per_page))
    return Page(
        per_page=query.per_page,
        results=chunks[query.page - 1],
        next=query.page + 1 if query.page < len(chunks) else None,
    )


class RetrieveRemoteData:
    def __init__(self, per_page: int = 3, page: int = 1) -> None:
        self.query = Query()
        self.page = request(self.query)
        self.count = 0

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> Any:
        if self.count >= len(self.page.results):
            if self.page.next is None:
                raise StopIteration

            self.query.page = self.page.next
            self.page = request(self.query)
            self.count = 0

        val = self.page.results[self.count]
        self.count += 1
        return val


class Fibo:
    def __init__(self, n: int) -> None:
        self.n = n
        self.count = 0
        self.a = 0
        self.b = 1

    def __iter__(self) -> Self:
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration

        val = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return val
