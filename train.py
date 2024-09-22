from src.data_loader import download
from src.preprocessing import import_data

def main():

  # Download the data
  download()

  # Process the data and return the dataframes
  dst, sunspots, solar_wind = import_data()

  # TODO: Consolidate the data
  
  # TODO: Split the data

  # TODO: Train different models

  # TODO: Compare the results of the different models

if __name__== '__main__':
  main()
