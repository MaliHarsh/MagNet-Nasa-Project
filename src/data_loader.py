import os
import pandas as pd

def download(data_dir = "data"):
    
    # Create a data/ directory if it doesn't exist
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Define the paths where the dataset should be located
    dataset_path = os.path.join(data_dir, "magnet-nasa.zip")
    extracted_folder = os.path.join(data_dir, "magnet-nasa")

    # Check if the dataset is already downloaded
    if not os.path.exists(dataset_path):
        # Download the dataset into the data/ directory
        os.system(f'kaggle datasets download -d kingabzpro/magnet-nasa -p {data_dir}')

    # Check if the dataset is already extracted
    if not os.path.exists(extracted_folder):
        # Unzip the dataset into the data/ directory
        os.system(f'unzip {dataset_path} -d {data_dir}')
    else:
        print("Dataset already extracted.")

