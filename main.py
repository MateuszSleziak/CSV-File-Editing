import pandas as pd

def get_new_column_names(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            new_names = []
            for line in lines:
                parts = line.split(": ")
                if len(parts) > 1:
                    new_name = parts[1].strip()
                    new_names.append(new_name)
                else:
                    new_names.append(None)
        return new_names
    except FileNotFoundError:
        print("The specified file does not exist.")
        return None
