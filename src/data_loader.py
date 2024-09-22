import os
import logging
from pathlib import Path
import subprocess

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def ensure_directory_exists(dir_path):
    """
    Ensure that the directory exists. If not, create it.
    """
    if not dir_path.exists():
        logging.info(f"Directory {dir_path} does not exist. Creating it.")
        dir_path.mkdir(parents=True, exist_ok=True)

def run_command(command):
    """
    Run a shell command and handle errors.
    """
    try:
        logging.info(f"Running command: {command}")
        subprocess.run(command, check=True, shell=True)
        logging.info(f"Command succeeded: {command}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {command}\nError: {e}")

def download_dataset_if_needed(dataset_path, data_dir):
    """
    Download the dataset if it doesn't already exist.
    """
    if not dataset_path.exists():
        logging.info("Dataset not found. Downloading...")
        command = f'kaggle datasets download -d kingabzpro/magnet-nasa -p {data_dir}'
        run_command(command)
    else:
        logging.info("Dataset already downloaded.")

def extract_dataset_if_needed(dataset_path, extracted_folder):
    """
    Extract the dataset if it's not already extracted.
    """
    if not extracted_folder.exists():
        logging.info("Extracting dataset...")
        command = f'unzip -o {dataset_path} -d {extracted_folder.parent}'  # Added the -o flag to overwrite without prompting
        run_command(command)
    else:
        logging.info("Dataset already extracted.")

def download(data_dir="data"):
    """
    Ensure the dataset is downloaded and extracted into the data directory.
    """
    data_path = Path(data_dir)
    dataset_path = data_path / "magnet-nasa.zip"
    extracted_folder = data_path / "magnet-nasa"
    
    # Ensure the data directory exists
    ensure_directory_exists(data_path)
    
    # Download dataset if not present
    download_dataset_if_needed(dataset_path, data_path)
    
    # Extract dataset if not already extracted
    extract_dataset_if_needed(dataset_path, extracted_folder)

# Example call to function
download()
