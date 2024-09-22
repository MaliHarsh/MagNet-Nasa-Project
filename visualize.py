from src.data_loader import download
from src.preprocessing import import_Data
from src.visualization import show_enhanced_visualization(data)
def main():

  # Download the data
  download()

  # Process the data and return the dataframes
  dst, sunspots, solar_wind = import_Data()

  # Visualize the data  
  cols_to_plot = ["bx_gse", "bx_gsm", "bt", "density", "speed", "temperature"]
  show_enhanced_visualization(solar_wind[cols_to_plot].iloc[:1000])

  

if __name__== '__main__':
  main()
