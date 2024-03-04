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

def edit_column_names(csv_file, new_names):
    try:
        data = pd.read_csv(csv_file)
        
        print("Current column names:")
        print(data.columns)
        
        if len(new_names) != len(data.columns):
            print("The number of new column names must be the same as the number of current columns.")
            return None

        for i, new_name in enumerate(new_names):
            if new_name is not None:
                data.rename(columns={data.columns[i]: new_name}, inplace=True)
        
        output_file = input("CSV file name to which you want to save the changes: ")
        data.to_csv(output_file, index=False)
        print("Column names have been updated and saved to the CSV file.")
    except FileNotFoundError:
        print("The specified file does not exist.")

if __name__ == "__main__":
    csv_file = input("Please provide the name of the CSV file: ")
    new_names_file = input("Please provide the name of the file containing the new column names: ")
    
    new_names = get_new_column_names(new_names_file)
    
    if new_names:
        edit_column_names(csv_file, new_names)
#MŚ