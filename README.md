# Virtual Leader: Module 1

### Dataset Overview

The dataset contains 1,410 entries with details about professionals, including their LinkedIn profiles, roles, organizations, locations, industries, and tenure. While most entries have role and location data, some fields like industry and organization ID have missing values. This dataset is ideal for analyzing professional networks, geographic trends, and career progression.

### Generating summarized corpus from dataset

LinkedIn data is processed using **spaCy** and **BART** to create a summarized corpus for each individual. Below are the key steps:

1. **Text Preparation**:
   - Extracts details such as LinkedIn name, role, organization, location, industry, tenure, and background.
   - Cleans the extracted text using spaCy by removing stopwords and punctuation.

2. **Summarization**:
   - Uses the BART model to generate a concise summary for each individual.
   - Configured with a beam search of 4 and a maximum output length of 150 tokens for high-quality summaries.

3. **Processing**:
   - Applies the summarization function to the first 500 rows of the dataset.
   - Creates a new column, `Corpus`, containing the generated summaries.

4. **Output**:
   - Saves the LinkedIn name and the summarized corpus into a CSV file named `summarized_corpus.csv`.

### Output File
The summarized corpus is saved as `summarized_corpus.csv`, containing:
- **LinkedIn Name**
- **Summarized Corpus**


### Generate Adjacency List from Summarized Corpus

The corpus data is processed to generate an adjacency list representing professional connections based on the summarized corpus. Below are the key steps:

1. **Input**:
   - The pre-summarized corpus is loaded from `summarized_corpus.csv`.

2. **Initialization**:
   - The script initializes an adjacency list using Python's `defaultdict`.

3. **Connection Simulation**:
   - Each person (node) is connected to a random number of other individuals (15–20 connections) using a normal distribution.
   - Connections avoid self-loops and are randomly assigned for each person.

4. **Output**:
   - A sample of the generated adjacency list is displayed, where each person is connected to several others.
   - The complete adjacency list is saved as `adjacency_list.json` for further analysis.


# BFS with Path Search

## Features
- Searches for a path from the starting node to the target node.
- Returns the sequence of nodes if a path exists, otherwise returns `None`.
- Also returns the summary for the target person.

## Functionality
- The function `bfs_with_path(start, target)` performs BFS and returns the path if found from start person to target person.


# Backend
main.py

A simple Flask-based API to find the shortest path between two nodes in a network using Breadth-First Search (BFS).

## Endpoints

### `GET /adjacency-list`
- **Description:** Returns the adjacency list (network connections).
- **Response:**
    ```json
    {
        "Alice": ["Bob", "Charlie", ...],
        "Bob": ["Alice", "David", ...],
        ...
    }
    ```

### `POST /search`
- **Description:** Accepts `start` and `target` nodes, and returns the BFS path.
- **Request Body:**
    ```json
    {
        "start": "Alice",
        "target": "David"
    }
    ```
- **Response (success):**
    ```json
    {
        "path": "Alice -> Bob -> David"
    }
    ```
- **Response (error):**
    ```json
    {
        "error": "No connection found."
    }
    ```

## Setup
1. Install Flask: `pip install flask`
2. Run the app: `python main.py`

# Frontend
templates/index.html

A simple web interface to find the shortest path between two nodes using the BFS Path Search API.

## Features
- Input fields for the starting and target names.
- Displays the path as a graph or shows an error message if no path is found.

## Usage
1. Enter the start and target node names.
2. Click **Search** to find the path.
3. View the graph or error message.
