from grid import Grid, Action, Position


def test_up():
    grid = Grid()
    grid.step(Action.UP)
    assert grid.position == Position(row=2, column=0)


def test_right():
    grid = Grid()
    grid.step(Action.RIGHT)
    assert grid.position == Position(row=3, column=1)


def test_down():
    grid = Grid()
    grid.step(Action.DOWN)
    assert grid.position == Position(row=4, column=0)


def test_left():
    grid = Grid()
    grid.step(Action.RIGHT)
    grid.step(Action.LEFT)
    assert grid.position == Position(row=3, column=0)


def test_border():
    grid = Grid()
    grid.step(Action.LEFT)
    assert grid.position == Position(row=3, column=0)

    grid.step(Action.UP)
    grid.step(Action.UP)
    grid.step(Action.UP)
    grid.step(Action.UP)
    assert grid.position == Position(row=0, column=0)

    grid = Grid()
    grid.step(Action.DOWN)
    grid.step(Action.DOWN)
    grid.step(Action.DOWN)
    grid.step(Action.DOWN)
    assert grid.position == Position(row=6, column=0)

    grid = Grid()
    grid.position = Position(row=3, column=9)
    grid.step(Action.RIGHT)
    assert grid.position == Position(row=3, column=9)


def test_reward():
    grid = Grid()
    reward = grid.step(Action.RIGHT)
    assert reward == -1

    grid = Grid()
    grid.position = Position(row=4, column=8)
    reward = grid.step(Action.LEFT)
    assert reward == 1


def test_wind():
    grid = Grid()
    grid.step(Action.RIGHT)
    grid.step(Action.RIGHT)
    grid.step(Action.RIGHT)
    grid.step(Action.RIGHT)
    assert grid.position == Position(row=2, column=4)
    grid.step(Action.RIGHT)
    assert grid.position == Position(row=1, column=5)


def test_is_terminal():
    grid = Grid()
    grid.position = Position(row=4, column=8)
    assert grid.is_terminal() is False
    grid.step(Action.LEFT)
    assert grid.is_terminal() is True
