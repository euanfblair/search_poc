Grant Matching Script
Description

This Python script is designed to match user queries with a list of grants. It reads grant data from a CSV file and uses OpenAI's GPT-4 to find grants that match the user's input based on their summaries.
Setup
Requirements

    Python 3.x
    openai Python package
    Access to OpenAI's API and a valid API key

Installation

    Ensure Python 3.x is installed on your system.
    Install the openai package using pip:

    pip install openai

API Key Configuration

    Obtain an API key from OpenAI.
    In the script, replace the api_key parameter's value with your actual OpenAI API key:

    python

    client = openai.OpenAI(api_key="YOUR_API_KEY_HERE")

Usage

    Prepare your grant data in a CSV file named grants_data.csv. The file should have columns for 'Name', 'Summary', and 'URL'.
    Run the script:

python grant_matching_script.py

When prompted, enter your grant search description or keywords.
The script will output matching grants based on the provided input 
# search_poc
