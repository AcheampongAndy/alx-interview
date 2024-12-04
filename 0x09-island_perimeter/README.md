# 0x09. Island Perimeter

## Description
This project involves solving a geometric problem using **Python** and **algorithmic logic**. The goal is to calculate the perimeter of a single island within a grid, represented as a 2D array of integers. The project strengthens your skills in navigating and manipulating 2D arrays, applying conditional logic, and designing efficient algorithms.

## Learning Objectives
By completing this project, you will:
- Understand how to work with **2D arrays (matrices)** in Python.
- Learn to navigate adjacent cells within a grid (horizontally and vertically).
- Apply **conditional logic** to determine cell contributions to the island’s perimeter.
- Develop counting techniques for calculating the perimeter.
- Enhance your **problem-solving** strategies for breaking down complex tasks into smaller, manageable steps.
- Reinforce Python programming concepts such as nested loops and logical conditions.

## Requirements
- **Environment**:
  - Ubuntu 20.04 LTS
  - Python 3.4.3
- **File Requirements**:
  - All files must end with a new line.
  - The first line of all Python scripts should be:
    ```python
    #!/usr/bin/python3
    ```
  - Code must follow the **PEP 8 style guide** (version 1.7).
  - Files must be **executable**.
- **Restrictions**:
  - No modules can be imported.
  - All modules and functions must be documented.

## Project Tasks
1. **Island Perimeter**:
   - Write a function that calculates the perimeter of a single island in a grid.
   - **Input**: A 2D grid where:
     - `0` represents water.
     - `1` represents land.
   - **Output**: The perimeter of the island.
   - **Algorithm**:
     - Iterate over all cells in the grid.
     - For each land cell (`1`), check its neighbors (top, bottom, left, right).
     - Count edges that contribute to the perimeter (i.e., edges adjacent to water or the grid boundary).
