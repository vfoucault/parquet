import unittest2
from hamcrest import *

from parquet.lame import Lame
from parquet.parquet import Parquet
from parquet.row import Row


class TestParquet(unittest2.TestCase):

    def test_get_last_row_should_give_last_row_if_not_first_row(self):
        # Given
        parquet = Parquet(width=300, length=300)
        row = Row(0, 100, 100)
        lame = Lame(200, 50, 'blue')
        row.add_lame(lame)
        parquet.add_row(row)

        # When
        last_row = parquet.get_last_row()

        # Then
        assert_that(last_row, is_(row))

    def test_get_last_row_should_give_None_if_first_row(self):
        # Given
        parquet = Parquet(width=300, length=300)

        # When
        last_row = parquet.get_last_row()

        # Then
        assert_that(last_row, is_(None))

    def test_add_row_should_update_row_numbers_and_self(self):
        # Given
        parquet = Parquet(width=300, length=300)
        row = Row(0, 100, 100)

        # When
        parquet.add_row(row)

        # Then
        assert_that(parquet.current_row, is_(1))
        assert_that(parquet.parquet[0], is_(row))

    def test_create_row_should_return_a_row_with_correct_params(self):
        # Given
        parquet = Parquet(width=300, length=300, lame_width=150)

        # When
        row = parquet.create_row()

        # Then
        assert_that(row.length, is_(300))
        assert_that(row.width, is_(150))
        assert_that(row.row_id, is_(0))

    def test_get_my_xs_should_return_the_good_coordinates(self):
        # Given
        parquet = Parquet(width=300, length=300, lame_width=10)
        row = Row(row_id=10, length=150, width=10)

        # When
        xs = parquet.get_my_xs(row)

        # Then
        assert_that(xs, is_((100, 110)))

    def test_fetch_good_length_should_remove_previous_lame_size_if_any(self):
        # Given
        parquet = Parquet(width=3000, length=3000)
        row = Row(0, 3000, 100)
        lame = Lame(1200, 50, 'blue')
        row.add_lame(lame)

        # When
        good_sizes = parquet.fetch_good_size(row)

        # Then
        assert_that(good_sizes, contains_inanyorder(850, 500, 350))

    def test_fetch_good_length_should_remove_previous_lame_color_if_any(self):
        # Given
        parquet = Parquet(width=3000, length=3000)
        parquet.colors = [ 'blue', 'red']
        row = Row(0, 3000, 100)
        lame = Lame(1200, 50, 'blue')
        row.add_lame(lame)

        # When
        good_colors = parquet.fetch_good_colors(row)

        # Then
        assert_that(good_colors, contains_inanyorder('red'))