from io import StringIO

import pandas as pd
from pandas import DataFrame
import re

def read_csv_section(filepath: str) -> DataFrame:
    # Read the contents of the CSV file as a regular text file
    with open(filepath, 'r') as file:
        lines = file.readlines()

    # Extract contents after the 10th line
    remaining_lines = lines[9:]

    # Join the remaining lines into a single string
    remaining_text = ''.join(remaining_lines)

    # Define your regex pattern to match the desired section
    regex_pattern = r'(?s)^(.*?)(?="Dataset: Motor Vehicle Census)'
    match = re.search(regex_pattern, remaining_text, re.DOTALL)

    extracted_section = match.group()

    # Remove 2nd line which is a title for the columns
    extracted_section = "\n".join(extracted_section.split("\n")[:1] + extracted_section.split("\n")[2:])

    # Convert the extracted section into a format that can be read as a CSV
    extracted_io = StringIO(extracted_section)
    df = pd.read_csv(extracted_io)

    df = df.rename(index={'Total': 'Total vehicles'})

    return df


for i in range(2013, 2021 + 1):
    filepath = f'./Datasets/motor_vehicle_fuel_vs_state_{i}.csv'
    result_dataframe = read_csv_section(filepath)
    if result_dataframe is not None:
        print(result_dataframe)
    else:
        print("Regex pattern didn't match in the file.")