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
    year_range = range(2013, 2021 + 1)
    for i in year_range:
        filepath = f'./Datasets/motor_vehicle_fuel_vs_state_{i}.csv'
        result_dataframe = read_csv_section(filepath)

        datasets.append(result_dataframe)

    # Identify unique row and column indices from all DataFrames
    all_rows = set()
    all_columns = set()
    for df in datasets:
        all_rows.update(list(df["State"]))
        all_columns.update(c for c in df.columns if c != "State" and not c.endswith(" - Annotations") and c != 'Unnamed: 19')

    year_frames = {i: {} for i in year_range}
    for df, year in zip(datasets, year_range):
        year_frames[year] = {c: {r:0 for r in all_rows} for c in all_columns}


    # Create a 3D DataFrame filled with 0
    shape = (len(all_rows), len(all_columns), len(datasets))
    result_data = np.zeros(shape, dtype=int)

    # Fill in the cells with values from the DataFrames
    # for i, df in enumerate(datasets):
    #     for row_idx, row in enumerate(df.index):
    #         for col_idx, col in enumerate(c for c in df.columns if c in all_columns):
    for df, year in zip(datasets, year_range):
        # Column
        for state in year_frames[year].keys():
            # Row
            for fuel_type in year_frames[year][state].keys():
                fuel_type_idx = df[df["State"] == fuel_type].index
                n_vehicles_array = df.loc[fuel_type_idx, state].values
                if n_vehicles_array.size == 0:
                    continue
                year_frames[year][state][fuel_type] = n_vehicles_array[0]

    # Convert the dictionary to a pandas DataFrame
    frames = []
    for year, frame_data in year_frames.items():
        frame = pd.DataFrame.from_dict(frame_data, orient='index')
        frames.append(frame)

    # Concatenate the frames along the third axis (depth)
    result_df = pd.concat(frames, axis=1, keys=year_frames.keys())

    # Fill missing values with 0
    result_df = result_df.fillna(0)

    print(result_df)
