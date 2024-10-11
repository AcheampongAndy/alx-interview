# Lockboxes

## Overview
This project solves the problem of determining if all lockboxes can be opened, starting with just one key for box 0. Each box may contain additional keys to other boxes, and the goal is to unlock all of them using Python. The project applies key concepts such as lists, recursion, graph traversal (DFS/BFS), and set operations.

## Requirements
- All code will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.
- Your code should conform to the PEP 8 style guide (version 1.7.x).
- All files must end with a new line.
- A `README.md` file at the root of the project folder is mandatory.
- All your files must be executable.

## Project Setup

1. Clone the repository:
    ```bash
    git clone <your-repo-url>
    cd lockboxes
    ```

2. Ensure all files are executable:
    ```bash
    chmod +x *.py
    ```

3. Make sure your script starts with the shebang line:
    ```bash
    #!/usr/bin/python3
    ```

4. Run your solution:
    ```bash
    ./<your_script>.py
    ```

## Key Concepts
- **Lists**: Used to store and manipulate keys and boxes.
- **Recursion/Iteration**: Either can be applied for traversing the boxes.
- **Graph Traversal (DFS/BFS)**: This project can be seen as a graph problem, where boxes are nodes, and keys represent edges.
- **Sets**: Used to track visited boxes and collected keys.

## Usage
Your program should:
1. Start with an initial key for box 0.
2. Collect additional keys from opened boxes.
3. Check if all boxes can be opened.

To execute the program, make sure all files are executable and follow this command in the terminal:

```bash
./lockboxes.py

