# Copyright (c) 2021 OM SANTOSHKUMAR MASNE.
# All Rights Reserved.
# Licensed under the MIT license.
# See LICENSE file in the project root for license information.

from collections import deque

from puzzle import test_goal


def bfs_search(hard_state):
    print("Using BFS")

    max_frontier_size = 0
    max_search_depth = 0

    frontier = deque()
    frontier.append(hard_state)

    explored = set()

    while frontier:
        state = frontier.popleft()
        explored.add(state.stateID)

        if test_goal(state.config):
            print("BFS SUCCESS")
            return (state, max_frontier_size, max_search_depth)

        branches = state.expand()

        for neighbour in branches:
            if neighbour.stateID not in explored:
                frontier.append(neighbour)
                explored.add(neighbour.stateID)

                if neighbour.cost > max_search_depth:
                    max_search_depth += 1

        if len(frontier) > max_frontier_size:
            max_frontier_size = len(frontier)

    return False
