import re, json, requests, csv, os
import pandas as pd
import matplotlib.pyplot as plt

data = []

with open('solutions.txt', 'r') as f:
    for line in f:
        data.append(line.strip())
    

print(data)

with open('solution_dictionary.json', 'w') as f1:
    json.dump(data, f1)