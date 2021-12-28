#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 17:29:40 2021

@author: sahmaran
"""

import os
os.listdir()

import pandas as pd
from scipy import random


file = pd.read_excel("evals.xls")  ### this file should be in the same directory as your python file


def return_comments(file, size = 10, seed = 0):
    """
    
    Parameters
    ----------
    file : this is a dataframe it should have value column that contais sentiments of given sentences
    size : int fixed = 10
  
    seed : random_seed to obtain the same every time you run this script

    Returns
    -------
    comments : 10 chosen comments
    average_polarity : average polarity of the chosen comments

    """
    len_ = len(file)
    indices = [i for i in range(len_)]
    random.seed(seed)
    chosen_indices = random.choice(indices, replace = False, size = size)
    comments = file.iloc[chosen_indices]
    average_polarity = sum(file.loc[chosen_indices,"Value"])/size
    return comments, average_polarity

if __name__ == "__main__":
    print(return_comments(file))
