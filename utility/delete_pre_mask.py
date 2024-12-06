import os
import glob

def delete_pre_disaster_json_files(folder_path):
    # Construct the pattern to match files ending with _pre_disaster.json
    pattern = os.path.join(folder_path, '*_pre_disaster_target.png')

    # Use glob to get a list of matching files
    files_to_delete = glob.glob(pattern)
    i = 0
    # Iterate over the list of files and delete each one
    for file_path in files_to_delete:
        try:
            os.remove(file_path)
            print(f"Deleted: {file_path}")
            i+=1
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")
    print(f"deleted {i} files")
# Example usage
folder_path = 'data/train/train1/targets'
delete_pre_disaster_json_files(folder_path)
