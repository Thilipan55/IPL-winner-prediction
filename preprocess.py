import pandas as pd
file_path = 'matches_updated_mens_ipl_upto_2024.csv'
try:
    df = pd.read_csv(file_path, parse_dates=['date'], dayfirst=True)
    print(f"Successfully loaded '{file_path}'.")
except FileNotFoundError:
    print(f"Error: file not found")
except Exception as e:
    print(f"An error occurred while loading the file: {e}")
    df = None

if df is not None:
    print(df.columns.tolist())
    print(f"Total columns: {len(df.columns)}")
    columns_to_drop = [
        'neutral_venue',
        'umpire1',
        'umpire2',
        'date1',
        'date2',
        'method',
        'reserve_umpire',
        'event',
        'gender',
        'match_referee',
        'tv_umpire'
    ]
    existing_columns_to_drop = [col for col in columns_to_drop if col in df.columns]
    df_cleaned = df.drop(columns=existing_columns_to_drop)
    print(df_cleaned.columns.tolist())
    print(f"Total columns: {len(df_cleaned.columns)}")
    df_cleaned.to_csv('cleaned_matches.csv', index=False)
