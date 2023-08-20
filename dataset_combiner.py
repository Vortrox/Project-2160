from io import StringIO

import pandas as pd
from pandas import DataFrame
import re
import numpy as np

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




if __name__ == "__main__":
    datasets = []
    for i in range(2013, 2021 + 1):
        filepath = f'./Datasets/motor_vehicle_fuel_vs_state_{i}.csv'
        result_dataframe = read_csv_section(filepath)

        datasets.append(result_dataframe)

    # Identify unique row and column indices from all DataFrames
    all_rows = set()
    all_columns = set()
    for df in datasets:
        all_rows.update(df.index)
        all_columns.update(df.columns)

    # Create a 3D DataFrame filled with 0
    shape = (len(all_rows), len(all_columns), len(datasets))
    result_data = np.zeros(shape, dtype=int)

    # Fill in the cells with values from the DataFrames
    for i, df in enumerate(datasets):
        for row_idx, row in enumerate(all_rows):
            for col_idx, col in enumerate(all_columns):
                if col == "State":
                    continue

                if row in df.index and col in df.columns:
                    if type(df.loc[row, col]) != str and np.isnan(df.loc[row, col]):
                        result_data[row_idx, col_idx, i] = 0
                    else:
                        result_data[row_idx, col_idx, i] = df.loc[row, col]

    # Create a MultiIndex for the columns
    multi_columns = pd.MultiIndex.from_tuples([(col, idx) for col in all_columns for idx in range(len(datasets))],
                                              names=['Column', 'DF Index'])

    # Create a 3D DataFrame using the result_data and multi_columns
    result_df = pd.DataFrame(result_data.reshape(shape[0], -1), index=list(all_rows), columns=multi_columns)

    print(result_df)