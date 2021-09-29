# Copyright (c) 2021 OM SANTOSHKUMAR MASNE.
# All Rights Reserved.
# Licensed under the MIT license.
# See LICENSE file in the project root for license information.

import sys
import math

from puzzle import PuzzleState
from bfs import bfs_search
from dfs import dfs_search
from ast_file import ast_search, ast_search_manhattan

import puzzle

max_search_depth = 0
max_frontier_size = 0


def bfs_solver(initial_state):
    result = bfs_search(initial_state)

    if result is False:
        print("BFS FAILED")
        return False

    global max_search_depth, max_frontier_size

    goal, max_frontier_size, max_search_depth = result

    return goal


def dfs_solver(initial_state):
    result = dfs_search(initial_state)

    if result is False:
        print("DFS FAILED")
        return False

    global max_search_depth, max_frontier_size

    goal, max_frontier_size, max_search_depth = result

    return goal


def a_star_solver(initial_state):
    result = ast_search(initial_state)

    if result is False:
        print("AST FAILED")
        return False

    global max_search_depth, max_frontier_size

    goal, max_frontier_size, max_search_depth = result

    return goal


def a_star_solver_manhattan(initial_state):
    result = ast_search_manhattan(initial_state)

    if result is False:
        print("AST FAILED")
        return False

    global max_search_depth, max_frontier_size

    goal, max_frontier_size, max_search_depth = result

    return goal


def backTrace(hard_state, goal_node):
    moves = []
    initial_state = hard_state
    current_state = goal_node

    print("BACKTRACING NOW...")
    print()

    while initial_state.config != current_state.config:
        moves.append(current_state.action)
        current_state = current_state.parent

    return moves


def writeOutput(hard_state, goal_node):
    moves = backTrace(hard_state, goal_node)
    moves.reverse()

    print("Solution: ")
    print(str(moves))
    print()

    print("Number of moves:" + str(len(moves)))
    print("Search Depth: " + str(goal_node.cost))
    print("Max search depth: " + str(max_search_depth))
    print("Max frontier size: " + str(max_frontier_size))
    print("Nodes expanded: " + str(puzzle.nodes_expanded))


def main():
    sm = sys.argv[1].lower()
    begin_state = sys.argv[2].split(",")

    begin_state = tuple(map(int, begin_state))
    size = int(math.sqrt(len(begin_state)))
    hard_state = PuzzleState(begin_state, size)

    if sm == "bfs":
        goal_node = bfs_solver(hard_state)
    elif sm == "dfs":
        goal_node = dfs_solver(hard_state)
    elif sm == "ast":
        goal_node = a_star_solver(hard_state)
    elif sm == "ast-man":
        goal_node = a_star_solver_manhattan(hard_state)
    else:
        print("Enter valid command arguments!")

    if goal_node is False:
        print("Unable to find solution.")
    else:
        writeOutput(hard_state, goal_node)


def puzzle_solver(puzzle_state, algorithm_to_use):
    begin_state = puzzle_state.split(",")
    begin_state = tuple(map(int, begin_state))
    size = int(math.sqrt(len(begin_state)))
    hard_state = PuzzleState(begin_state, size)

    if algorithm_to_use == "bfs":
        goal_node = bfs_solver(hard_state)
    elif algorithm_to_use == "dfs":
        goal_node = dfs_solver(hard_state)
    elif algorithm_to_use == "ast":
        goal_node = a_star_solver(hard_state)
    elif algorithm_to_use == "ast-man":
        goal_node = a_star_solver_manhattan(hard_state)
    else:
        print("Enter valid command arguments!")

    if goal_node is False:
        print("Unable to find solution.")
    else:
        moves = backTrace(hard_state, goal_node)
        moves.reverse()
        return moves


if __name__ == "__main__":
    main()
