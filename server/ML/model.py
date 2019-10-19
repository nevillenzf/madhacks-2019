from __future__ import absolute_import, division, print_function, unicode_literals

import pathlib2

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

import tensorflow as tf
import csv

from tensorflow import keras
from tensorflow.keras import layers

print("Loaded matplotlib, pandas, seaborn and tensorflow successfully.")

my_dict = []

with open('map.csv',"rb") as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0

    for row in csv_reader:
        my_dict.append(row)
    #analyze data row by row
    column_names = my_dict[0]

    raw_dataset = pd.read_csv('map.csv', names=column_names,
                      na_values = "?", comment='\t',
                      sep=" ", skipinitialspace=True)

    dataset = raw_dataset.copy()
    print(dataset)
    
    #split into train test sets
    train_dataset = dataset.sample(frac=0.8,random_state=0)
    test_dataset = dataset.drop(train_dataset.index)

    #sns.pairplot(train_dataset[["Company Name", "Disclosure Score", "Scope 1 (metric tonnes CO2e)", "Scope 2 (metric tonnes CO2e)"]], diag_kind="kde")
