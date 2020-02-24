#!/usr/bin/env python
# coding: utf-8
# This script is used to clean the generated complex terms : remove the pairs who have
import re, collections
from collections import Counter
import string
import csv



def removing(file):
    with open('/home/yizhewang/Bureau/manipulation/data_for_summer_work/data_for_summer_work/data_final/version_new/clean_pos.csv', "w") as csvfile:
        writer = csv.writer(csvfile, delimiter = ',')
        removed_lines = dict()
        with open(file) as csvfile:
            writein_lines = list()
            reader = csv.reader(csvfile, delimiter=',')
            counter = 0
            for row in reader:
                counter+=1

                #check if the pos of the same word are the same
                k1 = row[0].split()
                v1 = row[1].split()
                k2 = row[4].split()
                v2 = row[5].split()
                if k1[0] == k2[0] and v1[0] != v2[0]:
                    removed_lines["pos"+str(counter)] = row
                elif k1[0] == k2[-1] and v1[0] != v2[-1]:
                    removed_lines["pos"+str(counter)] = row
                elif k1[-1] == k2[0] and v1[-1] != v2[0]:
                    removed_lines["pos"+str(counter)] = row
                elif k1[-1] == k2[-1] and v1[-1] != v2[-1]:
                    removed_lines["pos"+str(counter)] = row
                else:
                    writein_lines.append(row)

            for item in writein_lines:
                writer.writerow(item)

        writer.writerow(["Removed lines:"])
        for k, v  in removed_lines.items():
            l = []
            l.append(k)
            l = l+v
            writer.writerow(l)
        print(counter)


#file = '/home/yizhewang/Bureau/manipulation/get_terme_ref/output/new/cterm_relation_addelmts.csv'
file = '/home/yizhewang/Bureau/manipulation/data_for_summer_work/data_for_summer_work/data_final/version_new/sym_removed.csv'
removing(file)
