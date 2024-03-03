import pandas as pd 

def file_name():
    csv = input("CSV File Name (File Must Be in the Same Folder as the Program):  ")

    try:
        data = pd.read_csv(csv)
    except FileNotFoundError:
        print("The specified file does not exist.")

file_name()
    

    

