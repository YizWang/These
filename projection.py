#!/usr/bin/env python
# coding: utf-8

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

def get_simpleterm_relation(ref):
    relations = []
    with open(ref, 'r', encoding="utf-8") as f:
        f.readline
        for line in f:
            if "Entrée" not in line:
                w1, pos1, w2, pos2, rel = line.strip().split(',')
                relations.append((w1, w2, rel))
    print(relations)
    return relations


def get_term(file):
    term_list_temp = []
    #read output of termsuite
    with open('/home/yizhewang/Bureau/manipulation/data_for_summer_work/data_for_summer_work/data_final/output_termsuite.tsv') as csvfile:
        reader = csv.reader(csvfile, delimiter='	')
        counter = 0
        for row in reader:
    #keep terms and remove variants
            if row[1] == "T" and int(row[5]) > 5:
                tag, term, spec, freq = row[2], row[3], row[6], row[5]
                term = term.strip()
                tag_temp=tag.split(" ")
                if len(tag_temp) == 2:
                    term_list_temp.append([term,tag, spec, freq])
                elif len(tag_temp) == 3 and "P" in tag:
                    term_list_temp.append([term, tag, spec, freq])
            elif row[1] == "T" and int(row[5]) <= 5:
                tag, term, spec, freq = row[2], row[3], row[6], row[5]
                tag_temp = tag.split(" ")
                if len(tag_temp) == 2:
                    counter+=1
                elif len(tag_temp) == 3 and "P" in tag:
                    counter+=1
    print(counter)

    return term_list_temp


def get_relation(relation_ref, list_term_corpus):
    with open('/home/yizhewang/Bureau/manipulation/data_for_summer_work/data_for_summer_work/data_final/get_term.csv', "w") as csvfile:
        writer = csv.writer(csvfile, delimiter = ',')
        term_rel = {}
        for w1, w2, rel in relation_ref:
            list_term1 = [t1 for t1 in list_term_corpus if w1 in t1[0].split() and w2 not in t1[0].split()]
            list_term2 = [t2 for t2 in list_term_corpus if w2 in t2[0].split() and w1 not in t2[0].split()]
            for it1 in list_term1:
                item1 = it1[0]
                l_item1 = item1.split()
                #l_pos1 = it1[1].split()
                m1, m2 = l_item1[0], l_item1[-1]
                # print(m1, m2)
                for it2 in list_term2:
                    item2 = it2[0]
                    l_item2 = item2.split()
                    #l_pos2 = it2[1].split()
                    m3, m4 = l_item2[0], l_item2[-1]
                    if m1 == m3:
                        result = it1 + it2
                        result.append(m2+" "+m4)
                        result.append("non permutation")
                        result.append(rel)
                        #result.append(pos_m1)
                        print(result)
                        writer.writerow(result)
                    elif m2 == m4:
                        result = it1 + it2
                        result.append(m1+" "+m3)
                        result.append("non permutation")
                        result.append(rel)
                        #result.append(pos_m2)
                        print(result)
                        writer.writerow(result)
                    elif m2 == m3:
                        result = it1 + it2
                        result.append(m1+" "+m4)
                        result.append("permutation")
                        result.append(rel)
                        #result.append(pos_m2)
                        print(result)
                        writer.writerow(result)
                    elif m1 == m4:
                        result = it1 + it2
                        result.append(m2+" "+m3)
                        result.append("permutation")
                        result.append(rel)
                        #result.append(pos_m1)
                        print(result)
                        writer.writerow(result)


    return term_rel





if __name__ == '__main__':
    ref = '/home/yizhewang/Bureau/manipulation/data_for_summer_work/data_for_summer_work/ref_FR.csv'
    file = '/home/yizhewang/Bureau/manipulation/get_terme_ref/list_terms/new/output_termsuite.tsv'
    #corpus = '/home/yizhewang/Bureau/manipulation/results_original/corpus.txt'
    #file_term = '/home/yizhewang/Bureau/results_original/output_term2.csv'
    relation_ref = get_simpleterm_relation(ref)
    list_term_corpus = get_term(file)
    #get_relation(relation_ref, list_term_corpus)
