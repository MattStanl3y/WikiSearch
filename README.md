# Wiki_Search

Wiki_Search is a simple Python script that allows users to search for information on Wikipedia topics directly from the command line.

## Project Goals

- Learn and implement virtual environments
- Learn and Practice web scraping using Python
- Interact with a public API (Wikipedia)
- Create a command-line interface that processes user input and handles network request errors.

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

This project contains a **_requirements.txt_** file. Here are the steps:

1. Make sure Python is installed on your system

2. Clone this repository

3. Create virtual environment:

   - On Windows:
     ```
     python -m venv venv
     ```
   - On macOS and Linux:
     ```
     python3 -m venv venv
     ```

4. Activate the virtual environment:

   - On Windows:
     ```
     .\venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

5. Install dependencies:

   - ```
     pip install -r requirements.txt
     ```

## Usage

With the virtual environment created, activated, and dependencies installed, run the script using Python:

```
python wiki_search.py
```

Follow the prompts to enter your search terms. The program will display the first paragraph of the corresponding Wikipedia article.

## Limitations

- The script only displays the first paragraph of the Wikipedia article.
- It may not work correctly for all Wikipedia pages due to potential variations in page structure.
