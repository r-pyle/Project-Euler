#Problem 22

#Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

#For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

#What is the total of all the name scores in the file?

#Answer = 871198282

#Solution

import pandas as pd
import string
import numpy as np

file = r'C:\Users\Ryan-Surface\OneDrive - River Road Asset Management\Documents\Projects\Project-Euler\extra\p022_names.txt'

data = pd.read_csv(file).columns.tolist()
data = sorted(data)
data_calc = []
alphabet = string.ascii_uppercase
total = []

def name_score(name):
    score = []
    for i in name:
        value = alphabet.index(i) + 1
        score.append(value)
    return np.sum(score)
    
for name in data:
    position = data.index(name) + 1
    score = name_score(name)
    total.append(score * position)

print(np.sum(total))