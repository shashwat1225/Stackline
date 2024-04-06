import json
import pandas as pd

def process_json_files(file_paths):
    dataframes = []

    for file_path in file_paths:
        with open(file_path) as file:
            data = json.load(file)

            # Find the key containing the student data
            student_key = None
            for key in data.keys():
                if isinstance(data[key], list) and data[key]:
                    student_key = key
                    break

            if student_key is None:
                raise ValueError(f"No valid student data found in file: {file_path}")

            df = pd.DataFrame(data[student_key])

            # Rename columns to normalized names
            column_mapping = {
                col: 'name' for col in df.columns if 'name' in col.lower()
            }
            column_mapping.update({
                col: 'age' for col in df.columns if 'age' in col.lower()
            })
            column_mapping.update({
                col: 'grade' for col in df.columns if 'grade' in col.lower()
            })
            df.rename(columns=column_mapping, inplace=True)

            # Ensure consistent data types
            df['name'] = df['name'].astype(str)
            df['age'] = pd.to_numeric(df['age'], errors='coerce')
            df['grade'] = df['grade'].astype(str)

            dataframes.append(df)

    # Combine DataFrames and handle missing values
    combined_df = pd.concat(dataframes, ignore_index=True)
    combined_df['age'].fillna(combined_df['age'].mean(), inplace=True)
    combined_df['grade'].fillna('Unknown', inplace=True)

    return combined_df

# Usage
file_paths = ['json1.json', 'json2.json']
result_df = process_json_files(file_paths)
print(result_df)