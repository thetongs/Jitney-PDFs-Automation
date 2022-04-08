# Load Libraries
import os
import shutil

# PDF Hunting 
def pdf_hunting(s_path, d_path):
    n_files = 0
    for root, dirs, files in os.walk(s_path):
        for file in files:
            if(str(file).endswith('.pdf')):
                shutil.copy(os.path.join(root,file), d_path)
                n_files = n_files + 1
    return n_files