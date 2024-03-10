import os
import json



def save_json_data(p_json_data: list,file_path):
    
    list_dict=[]
        
    #First load the data from the file.Initially file is empty so old_data is None
    old_data=load_data(file_path)  
    
    # Append new data from UI to existing data
    list_dict.append(p_json_data)
    
    #Concatenation happen when old data is not None
    if old_data is not  None:    
          list_dict=list_dict+old_data
    
    with open(file_path, 'w') as file:        
        #Saving the list of dictinaries as json format into the file
        json.dump(list_dict, file,indent=4)
        
        
def load_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    else:
        print("File does not exist")
    