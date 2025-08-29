import numpy as np
import pandas as pd
import matplotlib.pyplot as mlt
import json


#step 1 of the project
def merge_file(Us, In, Uk):
    Us['country'] = 'US'
    In['country'] = 'India'
    Uk['country'] = 'UK'
    # print(Us.head(5))
    # print(In.head(5))
    # print(Uk.head(5))
    
    merge_data = pd.concat([Us, In, Uk], ignore_index=True)
    return merge_data

#step 2 of the project
def messy_data_cleaning(file_data):
    
    # data_info = file_data.info()
    print('Project information : ')
    file_data.info()
    print(len(file_data))
    
    file_data = file_data.dropna(subset=['description'])
    file_data = file_data.drop_duplicates(subset=['video_id'])
    print('Null value checking', file_data.isnull().sum())
    print(len(file_data))
    
    #this is category_id according add on category for json file to      
    # Load the JSON file
    with open("datasetyoutube/US_category_id.json", "r") as f:
        category_data = json.load(f)
    # Build mapping dictionary
    category_mapping = {}
    for item in category_data["items"]:
        category_mapping[int(item["id"])] = item["snippet"]["title"]
        
    file_data['category'] = file_data['category_id'].map(category_mapping)
    
    
    print(file_data.head(5))
    return file_data

    
#3 Step of the project
def analysis(df):
    #top categories of the data
    india = df[df['country'] == 'India']
    uk = df[df['country'] == 'Uk']
    us = df[df['country'] == 'US']
    #this is data set for all category
    # print(india.head(2),'\n', uk.head(2), '\n', us.head(2))
    
    #top category check in country
    


if __name__ == "__main__":
    try:
        us_data = pd.read_csv('datasetyoutube/USvideos.csv')
        in_data = pd.read_csv('datasetyoutube/INvideos.csv')
        uk_data = pd.read_csv('datasetyoutube/GBvideos.csv')
        
        #checking data for all 
        # print('us Data \n', us_data.head(5))
        # print('In Data \n', in_data.head(5))
        # print('uk Data \n', uk_data.head(5))
        
        #This merge the all file 
        file_data = merge_file(us_data, in_data, uk_data)
        
        #messy data fix that
        clean = messy_data_cleaning(file_data)
        
        #insights/ analysis
        analysis(clean)
        
        
        
    except FileNotFoundError:
        print('File is Not Find')
        
    except FileExistsError:
        print("This File Doesn't Exists")
    else:
        print('Successful Work')