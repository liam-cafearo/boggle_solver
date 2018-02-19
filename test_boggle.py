import unittest
import boggle

class TestBoggle(unittest.TestCase):
    def test_Is_This_Thing_On(self):
        self.assertEqual(1, boggle.check())

    def test_can_create_an_empty_grid(self):
        grid = boggle.make_grid(0, 0)
        self.assertEqual(len(grid), 0)

    def test_grid_size_is_width_times_height(self):
        grid = boggle.make_grid(2, 3)
        self.assertEqual(len(grid), 6)