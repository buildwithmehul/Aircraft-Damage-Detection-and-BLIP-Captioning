import tarfile
import urllib.request 
import os 
import shutil

# URL of the tar file
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/ZjXM4RKxlBK9__ZjHBLl5A/aircraft-damage-dataset-v1.tar"

# Define the path to save the file 
tar_filename = "aircraft_damage_dataset_v1.tar" 
extracted_folder = "aircraft_damage_dataset_v1" # Folder where contents will be extracted

# Download the tar file 
urllib.request.urlretrieve(url, tar_filename) 
print(f"Downloaded {tar_filename}. Extraction will begin now.")

# Check if the folder already exists 
if os.path.exists(extracted_folder): 
    print(f"The folder '{extracted_folder}' already exists. Removing the existing folder.")

    # Remove the existing folder to avoid overwriting or duplication 
    shutil.rmtree(extracted_folder) 
    print(f"Removed the existing folder: {extracted_folder}")

# Extract the contents of the tar file 
with tarfile.open(tar_filename, "r") as tar_ref: 
    tar_ref.extractall() # This will extract to the current directory 
    print(f"Extracted {tar_filename} successfully.")


#The folder structure looks as follows:
"""
python
aircraft_damage_dataset_v1/
├── train/
│   ├── dent/
│   └── crack/
├── valid/
│   ├── dent/
│   └── crack/
└── test/
    ├── dent/
    └── crack/
    """