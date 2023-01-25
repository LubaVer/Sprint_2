from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_by_default_rating_by_default_one(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем книгу
        collector.add_new_book('Просто книга')
        # проверяем что по умолчанию рейтинг 1
        assert collector.get_book_rating('Просто книга')==1


    def test_set_book_rating_set_rating_ten(self):
        collector = BooksCollector()
        collector.add_new_book('Просто книга')
        collector.set_book_rating('Просто книга', 10)
        assert collector.get_book_rating('Просто книга')==10

    def test_set_book_rating_for_unknown_book_return_none(self):
        collector = BooksCollector()
        collector.add_new_book('Просто книга')
        collector.set_book_rating('Что делать, если ваш кот хочет вас убить', 10)
        assert collector.get_book_rating('Что делать, если ваш кот хочет вас убить') == None



    def test_set_book_rating_with_rating_zero_rating_dont_change(self):
        collector = BooksCollector()
        collector.add_new_book('Просто книга')
        collector.set_book_rating('Просто книга', 10)
        collector.set_book_rating('Просто книга', 0)
        assert collector.get_book_rating('Просто книга')==10

    def test_set_book_rating_with_rating_eleven_rating_dont_change(self):
        collector = BooksCollector()
        collector.add_new_book('Просто книга')
        collector.set_book_rating('Просто книга', 8)
        collector.set_book_rating('Просто книга', 11)
        assert collector.get_book_rating('Просто книга')==8

    def test_get_books_rating_show_all_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Просто книга')
        assert len(collector.get_books_rating())==3

    def test_get_books_with_specific_rating_list_wiht_rating_more_six(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Просто книга')
        collector.set_book_rating('Что делать, если ваш кот хочет вас убить', 10)
        collector.set_book_rating('Просто книга',6)
        assert collector.get_books_with_specific_rating(6)==['Просто книга'] and len(collector.get_books_with_specific_rating(6))

    def test_add_book_in_favorites_only_unique(self):
        collector = BooksCollector()
        collector.add_new_book('Просто книга')
        collector.add_book_in_favorites('Просто книга')
        collector.add_book_in_favorites('Просто книга')
        assert len(collector.get_list_of_favorites_books())==1

    def test_add_book_in_favorites_add_not_existing_book(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Просто книга')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_get_list_of_favorites_books_one_book_of_three(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Просто книга')
        collector.add_book_in_favorites('Просто книга')
        assert collector.get_list_of_favorites_books()==['Просто книга']

    def test_delete_book_from_favorites_one_book_of_two(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Просто книга')
        collector.add_book_in_favorites('Просто книга')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        collector.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')
        assert collector.get_list_of_favorites_books() == ['Просто книга']
