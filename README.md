# Tokenization and Data Normalization

## Overview

This project includes two main components:
1. `tokenizer.py`: A Python script that contains a function to tokenize and pad sentences given a vocabulary and desired sequence length.
2. `test_tokenizer.py`: A Python script that contains unit tests for the tokenizer file.
3. `df_normalizer.py`: A Python script that normalizes JSON data into a consistent DataFrame structure and combines them into a single DataFrame.

The goal is to demonstrate text processing and data manipulation using Python for natural language processing tasks and data science operations.

## Prerequisites
- Python 3.6+
- Pip package manager
- Virtual environment (recommended)

## Installation

1. Unzip the project folder and navigate to the project directory through the terminal.

2. Create a virtual environment (optional but recommended):

```bash
python3 -m venv env
```

3. Activate the virtual environment:

```bash
source env/bin/activate
```

4. Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

### Tokenizer

To run the tokenizer script on the test cases prodied as well as the ones created by me, run the following command:

```bash
python test_tokenizer.py
```

### Data Normalization

To run the data normalization script on the test cases provided as well as the ones created by me, run the following command:

```bash
python df_normalizer.py
```

