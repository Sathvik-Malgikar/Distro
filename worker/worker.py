import zipfile
import subprocess
import os
import shutil

def extract_zip_file(zip_file_path, extract_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

# Example usage
zip_file_path = 'worker.zip'
extract_path = 'Contents/'


import json
def write_checkpoint(epno ):
    
    with open("Contents/checkpoint.json", 'w+') as file:
        json.dump({"Completed epochs" : epno}, file)


def rename_chunks(directory="Contents/data/", prefix="chunk", extension=".csv"):

  for filename in os.listdir(directory):
    
    old_file_path = os.path.join(directory, filename)
    
    new_file_name = (directory + f"{prefix}{extension}")
    

    os.rename(old_file_path, new_file_name)

import os

import time
def create_worker_instance():

    subprocess.run(["docker",  "image", "build", "-t", "worker1", "."])

    # Run the docker command
    subprocess.run(["docker", "run" , "worker1"])


  
def spin_up():
    
    # Check if the folder exists
    if os.path.exists("Contents/"):
      # Delete the folder and its contents
      shutil.rmtree("Contents/")
    
    extract_zip_file(zip_file_path, extract_path)
    print("done extracting")
    rename_chunks()
    print("done renaming")
    create_worker_instance()
    print("done creating worker instance")
    
