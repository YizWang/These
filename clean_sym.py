#!/usr/bin/env python
# coding: utf-8
# This script is used to clean the generated complex terms : remove the pairs who have
import re, collections
from collections import Counter
import string
from collections import defaultdict
from sklearn.metrics import average_precision_score
import gensim
from gensim import models
import gensim.models.keyedvectors as word2vec
import numpy as np
from sklearn.metrics.pairwise import pairwise_distances
from sklearn.metrics.pairwise import cosine_similarity
import csv
from sklearn.preprocessing import label_binarize
from sklearn.metrics import average_precision_score
import pandas as pd
import subprocess
from gensim.models.phrases import Phrases, Phraser


def removing(file):
    with open('/home/yizhewang/Bureau/manipulation/data_for_summer_work/data_for_summer_work/data_final/clean_sym.csv', "w") as csvfile:
        writer = csv.writer(csvfile, delimiter = ',')
        removed_lines = dict()
        with open(file) as csvfile:
            writein_lines = set()
            reader = csv.reader(csvfile, delimiter=',')
            counter = 0
            for row in reader:
                copy_row = row.copy()
                counter+=1
                #check if the pos of the same word are the same

                if "_".join(row) not in writein_lines:
                    row[0], row[4] = row[4], row[0]
                    row[1], row[5] = row[5], row[1]
                    row[2], row[6] = row[6], row[2]
                    row[3], row[7] = row[7], row[3]
                    print(copy_row)
                    temp = row[8].split()
                    temp = temp[-1]+" "+temp[0]
                    row[8] = temp
                    print(row)
                    if "_".join(row) not in writein_lines:
                        writein_lines.add("_".join(copy_row))
                    else:
                        removed_lines["syme"+str(counter)] = copy_row
                else:
                    removed_lines["syme"+str(counter)] = copy_row
            for item in writein_lines:
                writer.writerow(item.split("_"))

        writer.writerow(["Removed lines:"])
        for k, v  in removed_lines.items():
            l = []
            l.append(k)
            l = l+v
            writer.writerow(l)
        print(counter)


file = '/home/yizhewang/Bureau/manipulation/data_for_summer_work/data_for_summer_work/data_final/get_term.csv'
removing(file)