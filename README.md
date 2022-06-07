# Wordle Solver

This program opens a Chrome instance of the wordle website and attempts to solve it for you. 

It's able to solve most words within the 6 attempts, but there are a few exceptions (see results.csv for the number of attempts each word requires)

## Requirements

- If on Windows: should be nothing, but if you run into issues please let me know!
- Othewise: Pip, Python, and Chrome installed on your computer

## Usage

If you're using Windows, simply double click on the world_solver alias within the root folder of the repository.

Otherwise, you'll need to run ``pip install -r requirements.txt`` from the root folder and then run the main.py script, which should look like ``python main.py``.

For all methods, a Google Chrome instance should pop up, load the Wordle website, and fill in words for you sequentially.



