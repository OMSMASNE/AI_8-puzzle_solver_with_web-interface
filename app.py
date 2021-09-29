# Copyright (c) 2021 OM SANTOSHKUMAR MASNE.
# All Rights Reserved.
# Licensed under the MIT license.
# See LICENSE file in the project root for license information.

from flask import Flask, render_template, request

import solver

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")


@app.route("/solve", methods=['POST'])
def solve():
    puzzle_state = request.form["puzzle_state"]
    algorithm_to_use = request.form["algorithm_to_use"]
    print("Puzzle state:", puzzle_state)
    print("Algorithm to use:", algorithm_to_use)

    steps = solver.puzzle_solver(puzzle_state, algorithm_to_use)

    for i in range(len(steps)):
        steps[i] = steps[i].upper()

    print("Solution steps:", str(steps))

    return str(steps)
