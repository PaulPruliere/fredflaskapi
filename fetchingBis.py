import numpy as np
import pandas as pd
from collections import Counter
from itertools import chain
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

def matches(path,df):
    """List each match attributes."""
    attributes = get_request_attributes(path)
    attributes = [a for a in attributes if a in df.columns.values] # keep valid attributes
    matches = [df.loc[df["{}".format(a)] == "x"].index for a in attributes]
    matches = [i for i in chain(*matches)] # flatten matches
    return matches

def get_histo(personalities,matches):
    """Build histogram of personalities matches"""
    histo = [0]*len(personalities)
    for k in matches:
        for i,j in enumerate(personalities):
            if k == j: histo[i] += 1
    return histo

def compute_error(histo):
    """Compute and spread 20 percent error on each attribute."""
    attr_error = [ (x*0.2)/((len(histo)-1)*0.8) for x in histo]
    error = [sum(attr_error)-attr for attr in attr_error]
    histo_error = [x+y for x,y in zip(histo,error)]
    return histo_error

def normalize(seq):
    """Normalize list."""
    normalized = [float(x)/sum(seq) for x in seq]
    return normalized

def threshold(matches,threshold=0.02):
    """Build an "others" category with small values."""
    others = reduce(lambda x,y: x+y,[matches[i] for i in matches if matches[i] < threshold])
    matches = {i:matches[i] for i in matches if matches[i] >= threshold}
    matches['others'] = others
    return matches

def jsonify_counter(counter):
    """Change counter to json array."""
    jarray = json.dumps([{"personality":i,"probability":j} for i,j in counter.items()])
    return jarray

def fetcher(path,spreadsheet):
    """Wrap all above functions."""
    # IMPORT VARIABLES
    df = import_data(spreadsheet)
    personalities = list(df.index)
    match = matches(path,df) 
    # CALCULATION
    normalized = normalize(compute_error(get_histo(personalities,match)))
    data = threshold(dict(zip(personalities,normalized)))
    return jsonify_counter(data)


