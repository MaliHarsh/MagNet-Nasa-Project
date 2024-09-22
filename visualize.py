from src.data_loader import download
from src.preprocessing import import_Data
from src.visualization import show_enhanced_visualization(data)
def main():

  # Download the data
  download()

  # Process the data and return the dataframes
  import_Data()

  # Visualize the data
  show_enhanced_visualization(data)

if __name__== '__main__':
  main()
