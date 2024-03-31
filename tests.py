import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):

        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    def test_get_book_genre_positive(self):

        collector = BooksCollector()
        collector.add_new_book('Задача трёх тел')
        collector.set_book_genre('Задача трёх тел', 'Фантастика')
        assert collector.get_book_genre('Задача трёх тел') == 'Фантастика'

    def test_set_book_genre_change_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Задача трёх тел')
        collector.set_book_genre('Задача трёх тел', 'Ужасы')
        collector.set_book_genre('Задача трёх тел', 'Фантастика')

        assert collector.get_book_genre('Задача трёх тел') == 'Фантастика'

    def test_add_new_book_no_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Задача трёх тел')

        assert collector.get_book_genre('Задача трёх тел') == ''

    def test_get_books_with_specific_genre_positive(self):
        collector = BooksCollector()
        collector.add_new_book('Задача трёх тел')
        collector.set_book_genre('Задача трёх тел', 'Фантастика')
        collector.add_new_book('Красная шапочка')
        collector.set_book_genre('Красная шапочка', 'Мультфильмы')
        collector.add_new_book('Ночной дозор')
        collector.set_book_genre('Ночной дозор', 'Фантастика')
        assert len(collector.get_books_with_specific_genre('Фантастика')) == 2

    def test_get_books_for_children_with_every_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Мастер и Маргарита')
        collector.set_book_genre('Мастер и Маргарита', 'Фантастика')
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние','Ужасы')
        collector.add_new_book('Пуаро')
        collector.set_book_genre('Пуаро','Детективы')
        collector.add_new_book('Дживс и Вустер')
        collector.set_book_genre('Дживс и Вустер', 'Комедии')
        collector.add_new_book('Капитан Врунгель')
        collector.set_book_genre('Капитан Врунегль','Мультфильмы')

        assert 'Сияние' and 'Пуаро' not in collector.get_books_for_children()

    def test_add_book_in_favorites_one_positive_one_negative(self):
        collector = BooksCollector()

        collector.add_new_book('Мастер и Маргарита')
        collector.set_book_genre('Мастер и Маргарита', 'Фантастика')
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        collector.add_new_book('Пуаро')
        collector.set_book_genre('Пуаро', 'Детективы')
        collector.add_new_book('Дживс и Вустер')
        collector.set_book_genre('Дживс и Вустер', 'Комедии')
        collector.add_new_book('Капитан Врунгель')
        collector.set_book_genre('Капитан Врунегль', 'Мультфильмы')

        collector.add_book_in_favorites('Мастер и Маргарита')
        collector.add_book_in_favorites('Ночной дозор')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_one_book(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Мастер и Маргарита')
        collector.delete_book_from_favorites('Мастер и Маргарита')
        assert len(collector.get_list_of_favorites_books()) == 0

    @pytest.mark.parametrize('genre', ['Мьюзиклы', 'Обучающие','Исторические'])
    def test_get_book_with_specific_genre_negative(self, genre):
        collector = BooksCollector()

        collector.add_new_book('Мастер и Маргарита')
        collector.set_book_genre('Мастер и Маргарита', 'Фантастика')
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        collector.add_new_book('Пуаро')
        collector.set_book_genre('Пуаро', 'Детективы')
        collector.add_new_book('Дживс и Вустер')
        collector.set_book_genre('Дживс и Вустер', 'Комедии')
        collector.add_new_book('Капитан Врунгель')
        collector.set_book_genre('Капитан Врунегль', 'Мультфильмы')

        assert collector.get_books_with_specific_genre(genre) == []

