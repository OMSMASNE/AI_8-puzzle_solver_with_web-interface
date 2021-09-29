# AI 8-puzzle solver with web-interface.

---

## Screen Recording:

### Web-Interface:
![Web-Interface](./Screen_Recordings/demo.gif?raw=true)

---

## USAGE:

### Requirements:
* Install the necessary requirements: `pip install -r requirements.txt`.

### Type the any of the following commands in the terminal as per the requirements:
* Dry run: `python solver.py algorithm_to_use board_pattern`
* Web Interface: `flask run`

---

### Supported algorithms:

1. AST = A * Search using total number of misplaced tiles heuristic.
2. AST-MAN = A * Search using total manhattan distance heuristic.
3. BSF = Breadth-First Search
4. DFS = Depth-First Search

## The web-interface uses "ast-man" algorithm.

### Board pattern examples:
1. "6,1,8,4,0,2,7,3,5"
2. "4,7,5,8,6,3,0,1,2"

### Dry run example:
```console
> python solver.py ast-man 4,7,5,8,6,3,0,1,2
Using AST - Manhattan distance
AST SUCCESS
BACKTRACING NOW...

Solution:
['Up', 'Right', 'Down', 'Left', 'Up', 'Right', 'Up', 'Right', 'Down', 'Down', 'Left', 'Up', 'Up', 'Right', 'Down', 'Left', 'Left', 'Up', 'Right', 'Down', 'Left', 'Up']

Number of moves:22
Search Depth: 22
Max search depth: 22
Max frontier size: 1128
Nodes expanded: 1857
```

---

## License:
### Licensed under the MIT license.

---

## Copyright (c) 2021 OM SANTOSHKUMAR MASNE.
## All Rights Reserved.
