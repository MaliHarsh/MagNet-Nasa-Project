#MagNet-Nasa-Project
from pathlib import Path
import pandas as pd
def import_Data():
  # Define the data path
  DATA_PATH = Path("data")
  
  # Load the dst_labels.csv dataset
  dst = pd.read_csv(DATA_PATH / "dst_labels.csv")
  dst.timedelta = pd.to_timedelta(dst.timedelta)
  dst.set_index(["period", "timedelta"], inplace=True)
  
  # Load the sunspots.csv dataset
  sunspots = pd.read_csv(DATA_PATH / "sunspots.csv")
  sunspots.timedelta = pd.to_timedelta(sunspots.timedelta)
  sunspots.set_index(["period", "timedelta"], inplace=True)
  
  # Load the solar_wind.csv dataset
  solar_wind = pd.read_csv(DATA_PATH / "solar_wind.csv")
  solar_wind.timedelta = pd.to_timedelta(solar_wind.timedelta)
  solar_wind.set_index(["period", "timedelta"], inplace=True)
  
  # Load the satelite_positions.csv dataset
  satelite_pos = pd.read_csv(DATA_PATH / "satelite_positions.csv")
  
  # Replace null values with the mean for each dataset
  for df in [dst, sunspots, solar_wind, satellite_positions]:
      numeric_cols = df.select_dtypes(include=['number']).columns
      df[numeric_cols].fillna(df[numeric_cols].mean(), inplace=True)
  return dst,sunspots,solar_wind
  


