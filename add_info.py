#!/usr/bin/env python
# coding: utf-8

import re, collections
from collections import Counter
import string
from collections import defaultdict
import csv

def deriv():
    with open('/home/yizhewang/Bureau/manipulation/data_for_summer_work/data_for_summer_work/data_final/derivation-tagged-valide.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        l = list()
        for row in reader:
            l.append(row)
    print(l)
    return l


def get_term(file, l):
    with open('/home/yizhewang/Bureau/manipulation/data_for_summer_work/data_for_summer_work/data_final/term_infoadded.csv',
              "w") as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        with open(file) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                term1, term2, dep = row[0], row[4], row[8]
                term1_temp = term1.split()
                term2_temp = term2.split()
                dep_temp = dep.split()
                if dep_temp[0] == term1_temp[0] and dep_temp[1] == term2_temp[0]:
                    row.insert(8, "T T")
                elif dep_temp[0] == term1_temp[0] and dep_temp[1] == term2_temp[-1]:
                    row.insert(8, "T E")
                elif dep_temp[0] == term1_temp[-1] and dep_temp[1] == term2_temp[0]:
                    row.insert(8, "E T")
                else:
                    row.insert(8, "E E")

                for i in l:
                    if dep_temp[0] == i[0] and dep_temp[1] == i[1]:
                        row.insert(11, i[2])
                        print(row)
                    elif dep_temp[0] == i[1] and dep_temp[1] == i[0]:
                        row.insert(11, i[2])
                        print(row)
                writer.writerow(row)


l = deriv()
#file = '/home/yizhewang/Bureau/manipulation/get_terme_ref/output/new/cterm_relation_addelmts.csv'
file = '/home/yizhewang/Bureau/manipulation/data_for_summer_work/data_for_summer_work/data_final/sym_cleaned.csv'
get_term(file, l)
