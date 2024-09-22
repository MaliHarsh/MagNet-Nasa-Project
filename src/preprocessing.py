#MagNet-Nasa-Project
from pathlib import Path
import pandas as pd
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_and_process_csv(file_name, data_path):
    """
    Load a CSV file, convert 'timedelta' to a time format, and set a multi-index.
    """
    logging.info(f"Loading {file_name} dataset.")
    df = pd.read_csv(data_path / file_name)
    
    # Check if 'timedelta' exists to convert it, otherwise skip
    if 'timedelta' in df.columns:
        df['timedelta'] = pd.to_timedelta(df['timedelta'])
    
    # Check if 'period' exists to set the index, otherwise skip
    if 'period' in df.columns and 'timedelta' in df.columns:
        df.set_index(['period', 'timedelta'], inplace=True)
    
    logging.info(f"{file_name} loaded and processed.")
    return df

def fill_missing_values(dfs):
    """
    Fill missing values with column means for numeric columns in a list of DataFrames.
    """
    for df_name, df in dfs.items():
        logging.info(f"Filling missing values for {df_name}.")
        numeric_cols = df.select_dtypes(include=['number']).columns
        df[numeric_cols].fillna(df[numeric_cols].mean(), inplace=True)
        logging.info(f"Missing values filled for {df_name}.")

def import_data():
    """
    Import multiple CSV datasets and process them.
    """
    DATA_PATH = Path("data")
    
    logging.info("Starting data import process.")
    
    # Define the datasets to load
    datasets = {
        "dst_labels.csv": "dst",
        "sunspots.csv": "sunspots",
        "solar_wind.csv": "solar_wind",
        "satellite_positions.csv": "satellite_positions"
    }
    
    # Load and process each dataset
    data_frames = {name: load_and_process_csv(file, DATA_PATH) for file, name in datasets.items()}
    
    # Fill missing values
    fill_missing_values(data_frames)
    
    logging.info("Data import and processing complete.")
    
    return data_frames["dst"], data_frames["sunspots"], data_frames["solar_wind"]

# Example call to function
import_data()
