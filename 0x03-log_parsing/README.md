# 0x03. Log Parsing

## Description
This project involves parsing and processing data streams in real-time using Python. The goal is to read log data from standard input (stdin), extract specific information from each line, compute relevant metrics, and handle interruptions gracefully (like CTRL + C). The focus is on concepts such as file I/O, signal handling, data processing, regular expressions, dictionaries, and exception handling in Python.

## Concepts and Skills Utilized
The following key concepts and Python features are leveraged in this project:

- **File I/O**: Reading data line by line from sys.stdin.
- **Signal Handling**: Handling keyboard interruption (CTRL + C) using Python's signal module.
- **Data Processing**: Parsing each log line to extract data, such as status codes and file sizes, and aggregating them to compute summaries.
- **Regular Expressions**: Validating log entry format using Python's re module.
- **Dictionaries**: Using dictionaries to count occurrences of HTTP status codes and accumulate total file sizes.
- **Exception Handling**: Handling potential errors during file reading and data processing.

## Project Requirements
- **Language**: Python 3.4.3
- **Operating System**: Ubuntu 20.04 LTS
- **Style**: Code must follow the PEP 8 guidelines (version 1.7.x).
- **Editors**: Use vi, vim, or emacs editors.
- **Executable Files**: All Python files must be executable and start with #!/usr/bin/python3.
- **Newline**: Each file must end with a new line.
- **File Length**: The length of files will be checked using wc.
