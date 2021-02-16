import random

import click

from grid import Grid, NUM_ROWS, NUM_COLS, Position, Action

GAMMA = 1


@click.command()
@click.option('--num-episodes', type=int, default=5000)
@click.option('--alpha', type=float, default=0.1)
@click.option('--epsilon', type=float, default=0.1)
def solve_windy_grid(num_episodes, alpha, epsilon):
    policy = sarsa(num_episodes, alpha, epsilon)
    print_greedy_policy(policy)


def sarsa(num_episodes, alpha, epsilon):
    q = initialize_policy()
    for episode in range(0, num_episodes):
        grid = Grid()
        state = grid.position
        action = choose_action(q, grid.position, epsilon)
        terminal = False
        while not terminal:
            reward = grid.step(action)
            state_prime = grid.position
            action_prime = choose_action(q, grid.position, epsilon)
            q[state][action.value] = q[state][action.value] + alpha * (
                    reward + GAMMA * q[state_prime][action_prime.value] - q[state][action.value])
            state = state_prime
            action = action_prime
            terminal = grid.is_terminal()
    return q


def initialize_policy() -> dict[Position, dict[int]]:
    result = {}
    for row in range(0, NUM_ROWS):
        for column in range(0, NUM_COLS):
            action_values = {}
            for action in Action:
                action_values[action.value] = 0
            result[Position(row=row, column=column)] = action_values
    return result


def choose_action(q: dict[Position, dict[int]], position: Position, epsilon: float) -> Action:
    if random.uniform(0, 1) < epsilon:
        return Action(random.randint(1, 4))
    action_values = q[position]
    return Action(max(action_values, key=action_values.get))


def print_greedy_policy(q: dict[Position, dict[int]]):
    for row in range(0, NUM_ROWS):
        for col in range(0, NUM_COLS):
            action_values = q[Position(row=row, column=col)]
            best_action = max(action_values, key=action_values.get)
            print(f'{best_action}', end=',')
        print()


if __name__ == '__main__':
    solve_windy_grid()
