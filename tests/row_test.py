import unittest2
from hamcrest import *

from parquet.lame import Lame
from parquet.row import Row


class TestRow(unittest2.TestCase):

    def test_check_space_should_return_true_if_enough_space_is_remaining(self):
        # Given
        row = Row(0, 100, 100)
        lame = Lame(50, 50, 'blue')
        # When
        enough_space = row.check_space(lame)

        # Then
        assert_that(enough_space, is_(True))

    def test_check_space_should_return_false_if_not_enough_space_is_remaining(self):
        # Given
        row = Row(0, 100, 100)
        lame = Lame(200, 50, 'blue')
        # When
        enough_space = row.check_space(lame)

        # Then
        assert_that(enough_space, is_(False))

    def test_get_last_lame_should_return_last_lame_if_exists(self):
        # Given
        row = Row(0, 100, 100)
        lame = Lame(10, 50, 'blue')
        row.add_lame(lame)
        # When
        last_lame = row.get_last_lame()

        # Then
        assert_that(last_lame, is_(lame))

    def test_get_last_lame_should_return_none_if_first_lame(self):
        # Given
        row = Row(0, 100, 100)

        # When
        last_lame = row.get_last_lame()

        # Then
        assert_that(last_lame, is_(None))

    def test_get_next_lame_id_should_return_0_if_first_lame(self):
        # Given
        row = Row(0, 100, 100)

        # When
        next_lame_id = row.get_next_lame_id()

        # Then
        assert_that(next_lame_id, is_(0))

    def test_get_next_lame_id_should_return_x_if_not_first_lame(self):
        # Given
        row = Row(0, 100, 100)
        lame = Lame(10, 50, 'blue')
        row.add_lame(lame)
        # When
        next_lame_id = row.get_next_lame_id()

        # Then
        assert_that(next_lame_id, is_(1))

    def test_add_lame_shoud_add_lame_and_update_space_left_and_self(self):
        # Given
        row = Row(0, 100, 100)
        lame = Lame(10, 50, 'blue')

        # When
        row.add_lame(lame)

        # Then
        assert_that(row.space_left, is_(90))
        assert_that(row.lames[0], is_(lame))

