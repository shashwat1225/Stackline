import json
import pandas as pd

def process_json_files(file_paths):
    dataframes = []

    for file_path in file_paths:
        with open(file_path) as file:
            data = json.load(file)

            if 'students' in data:
                df = pd.DataFrame(data['students'])
                df.rename(columns={'name': 'name', 'age': 'age', 'grade': 'grade'}, inplace=True)
            elif 'data' in data:
                df = pd.DataFrame(data['data'])
                df.rename(columns={'student_name': 'name', 'student_age': 'age', 'student_grade': 'grade'}, inplace=True)
            else:
                raise ValueError(f"Unexpected JSON structure in file: {file_path}")

            #Data type consistency
            df['name'] = df['name'].astype(str)
            df['age'] = pd.to_numeric(df['age'], errors='coerce')
            df['grade'] = df['grade'].astype(str)

            dataframes.append(df)

    #Handling missing values and merging the DFs
    combined_df = pd.concat(dataframes, ignore_index=True)
    combined_df['age'].fillna(combined_df['age'].mean(), inplace=True)
    combined_df['grade'].fillna('Unknown', inplace=True)

    return combined_df

#Usage
file_paths = ['json1.json', 'json2.json']
result_df = process_json_files(file_paths)
print(result_df)