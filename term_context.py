import csv
import codecs
from nltk.tokenize import word_tokenize
from collections import defaultdict


def process_reference(file_name):
    """
    input: reference file
    output: a set of reference complex terms

    """
    term_set = set()
    mot_set = set()

    with open(file_name, "r") as f:
        csv_reader = csv.reader(f, delimiter=',')
        for row in csv_reader:
            term_set.add(row[0])
            term_set.add(row[1])
        for term in term_set:
            t_tmp = term.split()
            mot_set.add("_".join(t_tmp))
    print(mot_set)
    return mot_set


def get_context(corpus_tagged, ref, n):
    context = defaultdict(set)
    with open(corpus_tagged, "r") as fh2:
        content = fh2.readlines()
    for term in ref:
        value = " ".join(term.split("_"))
        for line in content:
            if len(context[value])<=6:
                if " "+term+" " in line:
                    tokens = line.split(" ")
                    t_position = tokens.index(term)
                    if len(tokens) > n:
                        if t_position >= n and t_position + n <= len(tokens):
                            c = tokens[t_position - n:t_position + n]
                        elif t_position < n and t_position + n <= len(tokens):
                            c = tokens[:t_position + n]
                        elif t_position >= n and t_position + n > len(tokens):
                            c = tokens[t_position - n:]
                        else:
                            c = tokens
                        context[value].add(" ".join(c))
                    elif 6 < len(tokens) <= n:
                        context[value].add(line)
                    else:
                        print("toot short to be a context")
    return(context)

ref_file = '/home/yizhewang/Bureau/manipulation/lrec/data_annotation/lists_contexts2/qsyn_list.csv'
corpus_tagged = '/home/yizhewang/Bureau/manipulation/lrec/data_annotation/lists_contexts2/tagged_corpus.txt'
ref = process_reference(ref_file)
dico_tc = get_context(corpus_tagged, ref, 15)
print(dico_tc)

with open('/home/yizhewang/Bureau/manipulation/lrec/data_annotation/lists_contexts2/qsyn_list.csv', "r") as f:
    pair=list()
    csv_reader = csv.reader(f, delimiter=',')
    for row in csv_reader:
        set_temp=set()
        set_temp.add(row[0])
        set_temp.add(row[1])
        pair.append(set_temp)

with open('/home/yizhewang/Bureau/manipulation/lrec/data_annotation/lists_contexts2/qsyn_context.csv', "w") as csvfile:
    writer = csv.writer(csvfile, delimiter = ',')
    for x,y in pair:
        liste_temp = list()
        liste_temp.append(x+"&"+y)
        writer.writerow(liste_temp)
        value_x = dico_tc[x]
        value_y = dico_tc[y]
        if len(value_y) >= 5:
            for i in value_x:
                liste_temp = list()
                liste_temp.append(" ")
                liste_temp.append(i)
                writer.writerow(liste_temp)
            writer.writerow([""])
        else:
            print(x, y)
        if len(value_y) >= 5:
            for j in value_y:
                liste_temp = list()
                liste_temp.append(" ")
                liste_temp.append(j)
                writer.writerow(liste_temp)
        else:
            print(x, y)
     




