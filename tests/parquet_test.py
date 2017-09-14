import unittest2
from hamcrest import *

from parquet.parquet import Parquet


class TestParquet(unittest2.TestCase):

    def test_get_lame_size_should_give_a_different_lame_size_as_prev_one(self):
        # Given
        parquet = Parquet(width=300, length=300)
        parquet.lame_length = [150, 200]
        parquet.prev_lame.length = 150

        # When
        new_size = parquet.get_lame_size()

        # Then
        assert_that(new_size, equal_to(200))

    def test_get_lame_color_should_give_a_different_color_as_prev_one(self):
        # Given
        parquet = Parquet(width=300, length=300)
        parquet.colors = ['yellow', 'green']
        parquet.prev_lame.color = 'yellow'

        # When
        new_color = parquet.get_lame_color()

        # Then
        assert_that(new_color, equal_to('green'))
