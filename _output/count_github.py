import pandas as pd
import glob

files = glob.glob("*.csv")

total_count = 0  

for file in files:
    print(f"Processing {file}...") 
    
    try:
        chunk_size = 10000
        file_count = 0

        for chunk in pd.read_csv(file, chunksize=chunk_size):

            matches = chunk.astype(str).apply(lambda x: x.str.contains("GitHub", case=False, na=False)).any(axis=1)
            file_count += matches.sum()

        total_count += file_count 
        print(f"{file}: {file_count} lines contain 'GitHub'") 

    except Exception as e:
        print(f"Error processing {file}: {e}")  

print(f"Total lines containing 'GitHub': {total_count}")

