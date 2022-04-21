#!/usr/bin/env python
import sys
import os
import pandas as pd
import pymongo
import json
from pymongo import MongoClient

URI = 'mongodb+srv://sonmoogu:songiR!3911@cluster0.ch7uy.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

def import_content(filepath):
    mng_client = pymongo.MongoClient(URI)
    mng_db = mng_client['starbucks'] # Replace mongo db name
    collection_name = 'starbucks-collection' # Replace mongo db collection name
    db_cm = mng_db[collection_name]
    cdir = os.path.dirname(__file__)
    file_res = os.path.join(cdir, filepath)

    data = pd.read_csv(file_res)
    data_json = json.loads(data.to_json(orient='records'))
    #db_cm.remove()
    db_cm.insert_many(data_json)

if __name__ == "__main__":
  filepath = 'C:/Users/coding/CodeStates/Section3/Project/seoul_starbucks_df.csv'  # pass csv file path
  import_content(filepath)