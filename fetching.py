import numpy as np
import pandas as pd
from collections import Counter
import json
import requests

# import data spreadsheet as dataframe and reshape it
def import_data(spreadsheet):
    df = pd.read_csv(spreadsheet,header=1,index_col="Unnamed: 1")
    del df["Unnamed: 0"]
    df = df.T
    return df

# extract request attributes
def get_request_attributes(path):
    attributes = path.split('/')
    return attributes

# count how offen attributes match
def count_matches(path,df):
    attributes = get_request_attributes(path)
    attributes = [ a for a in attributes if a in df.columns.values] # keep valid attributes 
    matches = []
    for attr in attributes:
        matches.extend(df.loc[df["{}".format(attr)]=="x"].index)
    matches = dict(Counter(matches))
    return matches

# normalize counter values to add up up to 1
def normalize(counter):
    norm = sum(counter.values())
    counter.update((x,float(y)/norm) for x,y in counter.items())
    return counter

# change counter to json array
def jsonify_counter(counter):
    jarray = json.dumps([{"personality":i,"probability":j} for i,j in counter.items()])
    return jarray

# wrap up functions above return json array
def fetcher(path,spreadsheet):
    df = import_data(spreadsheet)
    probabilities = normalize(count_matches(path,df))
    return jsonify_counter(probabilities)