import numpy as np
import pandas as pd
from collections import Counter
import json
import requests

def import_data(spreadsheet):
    """Import data spreadsheet as dataframe and reshape it."""
    df = pd.read_csv(spreadsheet,header=1,index_col="Unnamed: 1")
    del df["Unnamed: 0"]
    df = df.T
    return df

def get_request_attributes(path):
    """Extract request attributes."""
    attributes = path.split('/')
    return attributes

def count_matches(path,df):
    """Count how offen attributes match."""
    attributes = get_request_attributes(path)
    attributes = [a for a in attributes if a in df.columns.values] #keep valid attributes only
    matches = []
    for attr in attributes:
        matches.extend(df.loc[df["{}".format(attr)]=="x"].index)
    matches = dict(Counter(matches))
    return matches

def normalize(counter):
    """Normalize counter values to add up up to 1."""
    norm = sum(counter.values())
    counter.update((x,float(y)/norm) for x,y in counter.items())
    return counter

def jsonify_counter(counter):
    """Change counter to json array."""
    jarray = json.dumps([{"personality":i,"probability":j} for i,j in counter.items()])
    return jarray

def fetcher(path,spreadsheet):
    """Wrap up functions above return json array."""
    df = import_data(spreadsheet)
    probabilities = normalize(count_matches(path,df))
    return jsonify_counter(probabilities)