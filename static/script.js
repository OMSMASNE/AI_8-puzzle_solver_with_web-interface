/*
Copyright (c) 2021 OM SANTOSHKUMAR MASNE.
All Rights Reserved.
Licensed under the MIT license.
See LICENSE file in the project root for license information.
*/

document.addEventListener("DOMContentLoaded", startup);

var delay_time = 200;
var algorithm_to_use = "ast-man";

function startup()
{
    document.getElementById("get-solution").addEventListener("click", get_solution);
    document.getElementById("play-solution").addEventListener("click", play_solution);
    document.getElementById("new-board").addEventListener("click", new_board);
}

function get_solution()
{
    document.getElementById('loader').style.display = "block";
    document.getElementById('solution-placeholder').style.display = "none";

    // let puzzle_state = "6,1,8,4,0,2,7,3,5";
    let puzzle_state = get_puzzle_state().result;

    let req = new XMLHttpRequest();
    req.open("POST", "/solve");

    let myForm = new FormData()
    myForm.append("puzzle_state", puzzle_state);
    myForm.append("algorithm_to_use", algorithm_to_use);
    req.send(myForm)
    req.onload = () => {
        console.log(req.responseText);
        solutionString = req.responseText;

        solutionString = solutionString.slice(1, solutionString.length - 1);
        solutionString = solutionString.replace(/[']/g, '');
        solutionArray = solutionString.split(",");

        document.getElementById("solution-box").innerText = "";

        document.getElementById('loader').style.display = "none";

        for(let i = 0; i < solutionArray.length; i++)
        {
            let element = document.createElement('div');
            element.innerText = solutionArray[i].trim();
            element.setAttribute('class', 'solution-element');
            element.setAttribute('id', 'solution-element-' + i);
            element.setAttribute('data-move', solutionArray[i].trim());

            document.getElementById("solution-box").append(element);
        }
    }
}

function play_solution()
{
    let num_steps = document.getElementById("solution-box").childElementCount;
    let current_step = 0;
    let intervalID = 0;

    if(num_steps == 0 || (current_step >= num_steps))
    {
        if(intervalID != 0)
        {
            clearInterval(intervalID);
        }
        return;
    }

    intervalID = setInterval(() => {
        if(current_step >= num_steps)
        {
            clearInterval(intervalID);
            return;
        }

        if(current_step > 0)
        {
            document.getElementById("solution-element-" + (current_step - 1)).classList.toggle('selected');
        }
        document.getElementById("solution-element-" + current_step).classList.toggle('selected');

        document.getElementById("solution-element-" + current_step).scrollIntoView();

        let current_move = document.getElementById("solution-element-" + current_step).dataset.move;

        play_move(current_move);

        current_step++;
    }, delay_time);
}

function play_move(move)
{
    let puzzle_state = get_puzzle_state().result.split(',');
    let blank_tile = get_puzzle_state().blank_tile;
    let target_tile;

    if(move == 'UP')
    {
        target_tile = blank_tile - 3;
        swap_tiles(puzzle_state, target_tile, blank_tile);
    }
    else if(move == 'DOWN')
    {
        target_tile = blank_tile + 3;
        swap_tiles(puzzle_state, target_tile, blank_tile);
    }
    else if(move == 'LEFT')
    {
        target_tile = blank_tile - 1;
        swap_tiles(puzzle_state, target_tile, blank_tile);
    }
    else if(move == 'RIGHT')
    {
        target_tile = blank_tile + 1;
        swap_tiles(puzzle_state, target_tile, blank_tile);
    }
}

function swap_tiles(puzzle_state, target_tile, blank_tile)
{
    let target_tile_value = puzzle_state[target_tile];
    document.getElementById("puzzle-board-" + target_tile).dataset.tile_value = 0;
    document.getElementById("puzzle-board-" + target_tile).innerText = '';

    document.getElementById("puzzle-board-" + blank_tile).dataset.tile_value = target_tile_value;
    document.getElementById("puzzle-board-" + blank_tile).innerText = target_tile_value;
}

function get_puzzle_state()
{
    let children = document.getElementById('puzzle-board').children;
    let result = "";
    let blank_tile = 0;

    for(let i = 0; i < children.length; i++)
    {
        if(i > 0)
        {
            result += ",";
        }
        result += children[i].dataset.tile_value;

        if(children[i].dataset.tile_value === '0')
        {
            blank_tile = i;
        }
    }

    return { result, blank_tile };
}

function new_board()
{
    document.getElementById('loader').style.display = "none";
    document.getElementById('solution-placeholder').style.display = "block";
    document.getElementById("solution-box").innerText = "";

    let available_values = [0, 1, 2, 3, 4, 5, 6, 7, 8];

    for(let i = 0; i <= 8; i++)
    {
        // Get a random value from the available_values.
        let value = available_values[Math.floor(Math.random() * (available_values.length - 0)) + 0];
        console.log(value);

        // Remove the used element.
        available_values.splice(available_values.indexOf(value), 1);

        document.getElementById("puzzle-board-" + i).dataset.tile_value = value;
        if(value == 0)
        {
            document.getElementById("puzzle-board-" + i).innerText = '';
        }
        else
        {
            document.getElementById("puzzle-board-" + i).innerText = value;
        }
    }
}
