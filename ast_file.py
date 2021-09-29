# Copyright (c) 2021 OM SANTOSHKUMAR MASNE.
# All Rights Reserved.
# Licensed under the MIT license.
# See LICENSE file in the project root for license information.

from heapq import heapify, heappop

from puzzle import test_goal, goal_state


def misplaced_tiles(state):
    num_misplaced_tiles = 0
    current_State = state

    for i, element in enumerate(current_State.config):
        if element != goal_state[i]:
            num_misplaced_tiles += 1

    return num_misplaced_tiles


def total_manhattan_distance(state):
    total = 0

    goal_pattern = {
        0: (0, 0), 1: (1, 0), 2: (2, 0),
        3: (0, 1), 4: (1, 1), 5: (2, 1),
        6: (0, 2), 7: (1, 2), 8: (2, 2)
    }

    cur_x = 0
    cur_y = 0
    for _, element in enumerate(state.config):
        if cur_x > 2:
            cur_x = 0
            cur_y += 1

        cur_num = int(element)

        total += abs(goal_pattern[cur_num][0] - cur_x) + abs(goal_pattern[cur_num][1] - cur_y)

        cur_x += 1

    return total


def ast_search_manhattan(hard_state):
    print("Using AST - Manhattan distance")

    max_frontier_size = 0
    max_search_depth = 0

    fn_heap = list()
    heap = list()

    frontier = list()
    frontier.append(hard_state)

    explored = set()
    explored.add(hard_state.config)

    while frontier:
        node = frontier.pop()
        explored.add(node.config)

        if test_goal(node.config):
            print("AST SUCCESS")
            return (node, max_frontier_size, max_search_depth)

        branches = node.expand()

        for neighbour in branches:
            if neighbour.config not in explored:
                fn = neighbour.cost + total_manhattan_distance(neighbour)

                explored.add(neighbour.config)
                fn_heap.append(fn)
                heap.append(neighbour)

                if neighbour.cost > max_search_depth:
                    max_search_depth += 1

        fnHeapCopy = list(fn_heap)
        heapify(fn_heap)
        fn_element = heappop(fn_heap)

        fn_element_index = fnHeapCopy.index(fn_element)
        fn_heap_element = heap.pop(fn_element_index)

        frontier.append(fn_heap_element)

        if len(heap) > max_frontier_size:
            max_frontier_size = len(heap)

    return False


def ast_search(hard_state):
    print("Using AST")

    max_frontier_size = 0
    max_search_depth = 0

    fn_heap = list()
    heap = list()

    frontier = list()
    frontier.append(hard_state)

    explored = set()
    explored.add(hard_state.config)

    while frontier:
        node = frontier.pop()

        if test_goal(node.config):
            print("AST SUCCESS")
            return (node, max_frontier_size, max_search_depth)

        branches = node.expand()

        for neighbour in branches:
            if neighbour.config not in explored:
                fn = neighbour.cost + misplaced_tiles(neighbour)

                explored.add(neighbour.config)
                fn_heap.append(fn)
                heap.append(neighbour)

                if neighbour.cost > max_search_depth:
                    max_search_depth += 1

        fnHeapCopy = list(fn_heap)
        heapify(fn_heap)
        fn_element = heappop(fn_heap)

        fn_element_index = fnHeapCopy.index(fn_element)
        fn_heap_element = heap.pop(fn_element_index)

        frontier.append(fn_heap_element)

        if len(heap) > max_frontier_size:
            max_frontier_size = len(heap)

    return False


if __name__ == "__main__":
    test = "7,2,4,5,0,6,8,3,1"
    begin_state = test.split(",")
    begin_state = tuple(map(int, begin_state))
    total_manhattan_distance(begin_state)
