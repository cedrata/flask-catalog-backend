import pytest

from api.common import Filter, Pagination
from api.data import MockedData


def test_catalog_id():
    """Test the behaviour when providing only catalog id."""
    md = MockedData()

    # invalid id: fails
    with pytest.raises(KeyError):
        md.get_prizes(0)

    # valid id with two items in catalog
    assert len(md.get_prizes(4)) == 2


def test_pagination():
    """Test the behaviour when paginating."""
    md = MockedData()

    assert (
        len(md.get_prizes(2, pagination=Pagination(page=1, per_page=2))) == 2
    )

    assert (
        len(md.get_prizes(2, pagination=Pagination(page=2, per_page=2))) == 1
    )

    assert (
        len(md.get_prizes(2, pagination=Pagination(page=1, per_page=40))) == 3
    )

    assert (
        len(md.get_prizes(2, pagination=Pagination(page=4, per_page=40))) == 0
    )


def test_filter():
    """Test the behaviour when filtering."""
    md = MockedData()

    # we expect only a result here
    res = md.get_prizes(1, prize_filter=Filter(id=1))
    assert len(res) == 1
