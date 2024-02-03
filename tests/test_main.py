import unittest
from src.main import get_user_input
from unittest.mock import patch


class TestUserInput(unittest.TestCase):
    @patch('src.main.inp')
    def test_user_input(self, mock_input):
        mock_input.return_value = "Nathaniel"
        self.assertEqual("dummy", get_user_input())


if __name__ == '__main__':
    unittest.main()
