import os

# Specify the folder containing your .txt files
folder_path = "PythonCodes"

# Iterate through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        # Construct the full file path
        old_file = os.path.join(folder_path, filename)
        # Replace .txt with .py
        new_file = os.path.join(folder_path, filename.replace(".txt", ".py"))
        # Rename the file
        os.rename(old_file, new_file)
        print(f"Renamed: {old_file} -> {new_file}")
