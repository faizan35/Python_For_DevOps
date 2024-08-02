'''
Q) Write a script to automate a simple task (e.g., renaming files in a directory)
'''


import os



x = os.listdir(r'E:\E - Downloads')


print(x)



def rename_files(folder_path, prefix):

  for filename in os.listdir(folder_path):
    # Get the full path of the file
    source_path = os.path.join(folder_path, filename)
    
    # Construct the new filename with the prefix
    new_filename = f"{prefix}_{filename}"
    
    # Get the full path of the renamed file
    destination_path = os.path.join(folder_path, new_filename)
    
    # Rename the file
    os.rename(source_path, destination_path)
    print(f"Renamed: {filename} to {new_filename}")

# Example usage
folder_path = "path/to/your/folder"
prefix = "renamed_"  # Prefix to add

rename_files(folder_path, prefix)
