import pickle
import pandas as pd
import argparse
import sys
import os
sys.path.append(os.path.abspath('./graph'))
sys.path.append(os.path.abspath('./utils'))
from graph import Graph
from utils import *
from node import Node


def read_dataset(fileName):
    """ Read the dataset and transform it to a dataframe
    Parameters
    ----------
    fileName: str
        file name that contains the dataset
    Retruns
    -------
    df: dataframe
        a dataframe to be classified
    """
    articles = pd.read_pickle(fileName)
    
    #Transforming the dataset to dataframe type to ease the operations on it
    df = df = pd.DataFrame({"title":[],"content":[],"topic":[]})
    for i in range(len(articles)):
        df = df.append({'title':articles[i]["title"],'content':articles[i]["content"],\
            'topic':articles[i]["topic"]},ignore_index=True)
    
    return df

def create_graph(data, n):
    G = Graph()
    for index, article in data.iterrows():
        G.add_node(Node(index, article["tokens"]))
    G.add_edges(n)
    return G


def main(fileName, n):
    df = read_dataset(fileName)
    df["tokens"] = df["content"].apply(lambda s: text2tokens(s))
    G = create_graph(df, n)
    connected_components = G.connected_components()
    for component in  connected_components:
	    print(component)
	    print("--------------------")
    


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("fileName", help="dataset file name", type=str)
    parser.add_argument("n", help="minimun nombre of tokens shared between two nodes to have an edge between them", type=int)
    args = parser.parse_args()
    main(args.fileName, args.n)
    
