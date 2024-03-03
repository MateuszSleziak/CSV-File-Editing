import pandas as pd 

csv = input("CSV file path: ")

try:
    data = pd.read_csv(csv)
except FileNotFoundError:
    print("The specified file does not exist.")

