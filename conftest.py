import pytest

from main import BooksCollector


@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector

@pytest.fixture
def collector_one_book(collector):
    collector.add_new_book('Просто книга')
    return collector

@pytest.fixture
def collector_two_books(collector_one_book):
    collector_one_book.add_new_book('Что делать, если ваш кот хочет вас убить')
    return collector_one_book