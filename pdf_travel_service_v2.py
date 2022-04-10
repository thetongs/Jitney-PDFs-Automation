# Load Libraries
import os
import shutil
import pandas as pd

# PDF Hunting 
file_names = []
def pdf_hunting(s_path, d_path):
    n_files = 0
    for root, dirs, files in os.walk(s_path):
        for file in files:
            if(str(file).endswith('.pdf')):
                file_names.append(file)
                # Select Folders After Base Folders as Destination Folder
                second_folder_name = os.path.join(root,file).split("\\")[1]
                # Check File From Base Folder
                if(len(os.path.join(root,file).split("\\")) == 2):
                    shutil.copy(os.path.join(root,file), (d_path))
                    n_files = n_files + 1
                # Check Second Folder Exists and Copy
                elif(os.path.exists(d_path+"/"+second_folder_name)):
                    shutil.copy(os.path.join(root,file), (d_path + "/"+ second_folder_name +"/"))
                    n_files = n_files + 1
                else:
                    # Create Folder and Copy
                    os.mkdir(d_path+"/"+second_folder_name)
                    shutil.copy(os.path.join(root,file), (d_path + "/"+ second_folder_name +"/"))
                    n_files = n_files + 1
    
    source_file_frame = pd.DataFrame(file_names, columns = ["File Names"])
    source_file_frame.to_csv(d_path + "/" + (s_path.split("/")[-1]+".csv"), index = False)

    return n_files