from collections import namedtuple
from enum import Enum

Position = namedtuple('Position', 'row column')

NUM_ROWS = 7
NUM_COLS = 10
START = Position(row=3, column=0)
GOAL = Position(row=3, column=7)


class Action(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4


class Grid:
    def __init__(self):
        self.position: Position = START

    def step(self, action: Action) -> int:
        self.position = self._next_position(action)
        if self.position == GOAL:
            return 1
        return -1

    def is_terminal(self):
        return self.position == GOAL

    def _next_position(self, action: Action) -> Position:
        result = self.position
        if result.column == 3 or result.column == 4 or result.column == 5 or result.column == 8:
            result = Position(row=result.row - 1, column=result.column)
        if result.column == 6 or result.column == 7:
            result = Position(row=result.row - 2, column=result.column)
        if action == Action.UP:
            result = Position(row=result.row - 1, column=result.column)
        elif action == Action.RIGHT:
            result = Position(row=result.row, column=result.column + 1)
        elif action == Action.DOWN:
            result = Position(row=result.row + 1, column=result.column)
        elif action == Action.LEFT:
            result = Position(row=result.row, column=result.column - 1)
        if result.column < 0:
            result = Position(row=result.row, column=0)
        if result.column >= NUM_COLS:
            result = Position(row=result.row, column=NUM_COLS - 1)
        if result.row < 0:
            result = Position(row=0, column=result.column)
        if result.row >= NUM_ROWS:
            result = Position(row=NUM_ROWS - 1, column=result.column)

        return result
