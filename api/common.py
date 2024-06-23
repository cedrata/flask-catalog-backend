from typing import NotRequired, TypedDict


# Query parameters
class Filter(TypedDict):
    id: NotRequired[int]
    description: NotRequired[str]


class Pagination(TypedDict):
    page: int
    per_page: int
