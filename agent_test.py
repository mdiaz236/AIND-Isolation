"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent
import sample_players
from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2)

    def test_first_player(self):
        self.assertEqual(self.game.active_player,'Player1')

    def test_initial_board(self):
        self.assertEqual(len(self.game.get_legal_moves()), 49)

class MiniMaxTest(unittest.TestCase):
    """Unit tests for minimax player"""

    def setUp(self):
        reload(game_agent)
        self.player1 = game_agent.MinimaxPlayer()
        self.player2 = sample_players.GreedyPlayer()
        self.game = isolation.Board(self.player1, self.player2)

    def test_move_works(self):
        result = self.game.play()

        self.assertIsNotNone(result)

    ## test that the best move is chosen?

    ## check the depth

if __name__ == '__main__':
    unittest.main()
