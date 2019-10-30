

import unittest

from parameterized import parameterized

from tateti import TaTeTi


class TaTeTiTest(unittest.TestCase):

    def test_initilization(self):

        tateti = TaTeTi()

        first = [' ' for _ in range(9)]

        self.assertEqual(tateti.board, first)

    @parameterized.expand([

        ([['x', 'o', 'x', 'o', 'x', 'o', 'x', 'o', 'x']]),

        ([['o', 'x', 'o', 'x', 'o', 'x', 'o', 'x', 'o']]),

        ([['x', 'x', 'o', 'o', 'x', 'x', 'o', 'o', 'x']]),

        ([['o', 'o', 'x', 'x', 'o', 'o', 'x', 'x', 'o']]),

        ([['o', 'x', 'x', 'o', 'o', 'x', 'x', 'o', 'o']]),

        ([['x', 'o', 'o', 'x', 'x', 'o', 'o', 'x', 'x']])

    ])
    def test_full(self, board):

        tateti = TaTeTi(board)

        self.assertTrue(tateti.full())

    @parameterized.expand([

        ([['x', 'o', 'x', 'o', ' ', 'o', 'x', 'o', 'x']]),

        ([['o', 'x', 'o', ' ', 'o', ' ', 'o', 'x', 'o']]),

        ([['x', 'x', 'o', ' ', 'x', 'x', ' ', ' ', 'x']]),

        ([['o', ' ', 'x', ' ', 'o', ' ', 'x', ' ', 'o']]),

        ([[' ', ' ', 'x', ' ', 'o', 'x', ' ', 'o', ' ']]),

        ([['x', ' ', ' ', 'x', ' ', ' ', 'o', ' ', ' ']])

    ])
    def test_not_full(self, board):

        tateti = TaTeTi(board)

        self.assertFalse(tateti.full())

    @parameterized.expand([

        ([['x', 'x', 'x', ' ', ' ', ' ', ' ', ' ', ' ']]),

        ([['o', 'o', 'o', ' ', ' ', ' ', ' ', ' ', ' ']]),

        ([[' ', ' ', ' ', 'x', 'x', 'x', ' ', ' ', ' ']]),

        ([[' ', ' ', ' ', 'o', 'o', 'o', ' ', ' ', ' ']]),

        ([[' ', ' ', ' ', ' ', ' ', ' ', 'x', 'x', 'x']]),

        ([[' ', ' ', ' ', ' ', ' ', ' ', 'o', 'o', 'o']]),

        ([['x', ' ', ' ', 'x', ' ', ' ', 'x', ' ', ' ']]),

        ([['o', ' ', ' ', 'o', ' ', ' ', 'o', ' ', ' ']]),

        ([[' ', 'x', ' ', ' ', 'x', ' ', ' ', 'x', ' ']]),

        ([[' ', 'o', ' ', ' ', 'o', ' ', ' ', 'o', ' ']]),

        ([[' ', ' ', 'x', ' ', ' ', 'x', ' ', ' ', 'x']]),

        ([[' ', ' ', 'o', ' ', ' ', 'o', ' ', ' ', 'o']]),

        ([['x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x']]),

        ([[' ', ' ', 'x', ' ', 'x', ' ', 'x', ' ', ' ']]),

        ([['o', ' ', ' ', ' ', 'o', ' ', ' ', ' ', 'o']]),

        ([[' ', ' ', 'o', ' ', 'o', ' ', 'o', ' ', ' ']])

    ])
    def test_win(self, board):

        tateti = TaTeTi(board)

        self.assertTrue(tateti.win())

    @parameterized.expand([

        ([['x', 'x', 'o', 'x', ' ', ' ', ' ', ' ', ' ']]),

        ([['o', 'o', ' ', ' ', 'x', ' ', ' ', ' ', ' ']]),

        ([[' ', ' ', 'x', 'o', 'x', 'x', ' ', ' ', ' ']]),

        ([[' ', ' ', ' ', 'o', 'o', 'x', 'o', ' ', ' ']]),

        ([[' ', 'x', ' ', ' ', ' ', ' ', 'o', 'x', 'x']]),

        ([[' ', ' ', 'o', ' ', ' ', ' ', 'x', 'o', 'o']]),

        ([['x', ' ', ' ', 'x', ' ', ' ', 'o', ' ', ' ']]),

        ([['o', ' ', ' ', 'o', ' ', ' ', 'x', ' ', ' ']]),

        ([[' ', 'x', ' ', ' ', 'o', ' ', ' ', 'x', ' ']]),

        ([[' ', 'o', ' ', ' ', 'x', ' ', ' ', 'o', ' ']]),

        ([[' ', ' ', 'x', ' ', ' ', 'o', ' ', ' ', 'x']]),

        ([[' ', ' ', 'o', ' ', ' ', 'x', ' ', ' ', 'o']]),

        ([['x', ' ', ' ', ' ', 'o', ' ', ' ', ' ', 'x']]),

        ([[' ', ' ', 'x', ' ', 'o', ' ', 'x', ' ', ' ']]),

        ([['o', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'o']]),

        ([[' ', ' ', 'o', ' ', 'x', ' ', 'o', ' ', ' ']])

    ])
    def test_not_win(self, board):

        tateti = TaTeTi(board)

        self.assertFalse(tateti.win())

    @parameterized.expand([

        (['x', 'o', 'x', 'o', ' ', 'o', 'x', 'o', 'x'], 4),

        (['o', 'x', 'o', ' ', 'o', ' ', 'o', 'x', 'o'], 3),

        (['x', 'x', 'o', ' ', 'x', 'x', ' ', ' ', 'x'], 6),

        (['o', ' ', 'x', ' ', 'o', ' ', 'x', ' ', 'o'], 1),

        ([' ', ' ', 'x', ' ', 'o', 'x', ' ', 'o', ' '], 0),

        (['x', ' ', ' ', 'x', ' ', ' ', 'o', ' ', ' '], 5)

    ])
    def test_validate(self, board, position):

        tateti = TaTeTi(board)

        self.assertTrue(tateti.validate(position + 1))

    @parameterized.expand([

        (['x', 'o', 'x', 'o', ' ', 'o', 'x', 'o', 'x'], 3),

        (['o', 'x', 'o', ' ', 'o', ' ', 'o', 'x', 'o'], 2),

        (['x', 'x', 'o', ' ', 'x', 'x', ' ', ' ', 'x'], 5),

        (['o', ' ', 'x', ' ', 'o', ' ', 'x', ' ', 'o'], 0),

        ([' ', ' ', 'x', ' ', 'o', 'x', ' ', 'o', ' '], 2),

        (['x', ' ', ' ', 'x', ' ', ' ', 'o', ' ', ' '], 6)

    ])
    def test_not_validate(self, board, position):

        tateti = TaTeTi(board)

        self.assertFalse(tateti.validate(position + 1))

    @parameterized.expand([

        (['x', 'o', 'x', 'o', ' ', 'o', 'x', 'o', 'x'], 3, 'x'),

        (['o', 'x', 'o', ' ', 'o', ' ', 'o', 'x', 'o'], 2, 'x'),

        (['x', 'x', 'o', ' ', 'x', 'x', ' ', ' ', 'x'], 5, 'x'),

        (['o', ' ', 'x', ' ', 'o', ' ', 'x', ' ', 'o'], 0, 'x'),

        ([' ', ' ', 'x', ' ', 'o', 'x', ' ', 'o', ' '], 2, 'x'),

        (['x', ' ', ' ', 'x', ' ', ' ', 'o', ' ', ' '], 6, 'x')

    ])
    def test_assign_invalid(self, board, position, piece):

        tateti = TaTeTi(board)

        with self.assertRaises(Exception):

            tateti.assign(position + 1, piece)

    @parameterized.expand([

        (5, 'x', ['x', 'o', 'x', 'o', ' ', 'o', 'x', 'o', 'x'],

         ['x', 'o', 'x', 'o', 'x', 'o', 'x', 'o', 'x']),

        (4, 'o', ['o', 'x', 'x', ' ', 'x', ' ', 'o', 'x', 'o'],

         ['o', 'x', 'x', 'o', 'x', ' ', 'o', 'x', 'o'])

    ])
    def test_assign(self, position, piece, board_old, board_new):

        tateti = TaTeTi(board_old)

        tateti.assign(position, piece)

        self.assertEqual(tateti.board, board_new)

    @parameterized.expand([

        (['x', 'o', 'x', 'o', ' ', 'o', 'x', 'o', 'x'],

         '\n x | o | x \n---+---+---\n o | 5 | o \n---+---+---\n x | o | x \n'),

        ([' ', ' ', 'x', ' ', 'o', 'x', ' ', 'o', ' '],

         '\n 1 | 2 | x \n---+---+---\n 4 | o | x \n---+---+---\n 7 | o | 9 \n'),

        ([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],

         '\n 1 | 2 | 3 \n---+---+---\n 4 | 5 | 6 \n---+---+---\n 7 | 8 | 9 \n')

    ])
    def test_draw_board(self, board, display):

        tateti = TaTeTi(board)

        self.assertEqual(tateti.draw_board(), display)


if __name__ == '__main__':

    unittest.main()
