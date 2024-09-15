import os
import pandas as pd

def download():
    # Create a data/ directory if it doesn't exist
    data_dir = "data"
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

    # Load and process CSV files
    dst = pd.read_csv(os.path.join(extracted_folder, "dst_labels.csv"))
    dst['timedelta'] = pd.to_timedelta(dst['timedelta'])
    dst.set_index(["period", "timedelta"], inplace=True)

    sunspots = pd.read_csv(os.path.join(extracted_folder, "sunspots.csv"))
    sunspots['timedelta'] = pd.to_timedelta(sunspots['timedelta'])
    sunspots.set_index(["period", "timedelta"], inplace=True)

    solar_wind = pd.read_csv(os.path.join(extracted_folder, "solar_wind.csv"))
    solar_wind['timedelta'] = pd.to_timedelta(solar_wind['timedelta'])
    solar_wind.set_index(["period", "timedelta"], inplace=True)

    satellite_positions = pd.read_csv(os.path.join(extracted_folder, "satellite_positions.csv"))

    # Replace null values with the mean for numeric columns only
    for df in [dst, sunspots, solar_wind, satellite_positions]:
        numeric_cols = df.select_dtypes(include=['number']).columns
        df[numeric_cols].fillna(df[numeric_cols].mean(), inplace=True)

    return dst, sunspots, solar_wind, satellite_positions

# Call the download function
dst, sunspots, solar_wind, satellite_positions = download()
