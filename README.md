# Wiki_Search

Wiki_Search is a simple Python script that allows users to search for information on Wikipedia topics directly from the command line.

## Goals of this project

- Learn and implement virtual environments
- Learn and Practice web scraping using Python
- Interact with a public API (Wikipedia)
- Build a command-line interface for user interaction
- Handle and process user input
- Implement error handling for network requests

## Features

- Interactive command-line interface
- Searches Wikipedia based on user input
- Displays the first relevant paragraph of the Wikipedia article
- Option to perform multiple searches in one session

## Requirements

- Python 3.x installed on your system
- Virtual environment (venv) with pre-installed libraries:
  - `requests`
  - `beautifulsoup4`

## Setup

This project uses a virtual environment with all required libraries pre-installed, here are the _steps to run the virtual enviornment_:

1. Ensure Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/downloads/) if needed.

2. Clone this repository or download the script and associated virtual environment.

3. Activate the virtual environment:

   - On Windows:
     ```
     .\venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

   When activated, your command prompt should change to indicate that you're now working within the virtual environment.

## Usage

With the virtual environment activated, run the script using Python:

```
python wiki_search.py
```

Follow the prompts to enter your search terms. The program will display the first paragraph of the corresponding Wikipedia article.

## How it works

1. The script takes user input for a search term.
2. It constructs a Wikipedia URL based on the input.
3. It sends a request to the Wikipedia page and scrapes the content.
4. The first non-empty paragraph from the main content is extracted and displayed.
5. Users can choose to perform additional searches or exit the program.

## Limitations

- The script only displays the first paragraph of the Wikipedia article.
- It may not work correctly for all Wikipedia pages due to potential variations in page structure.
