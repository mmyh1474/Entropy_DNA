import sys
import math
import csv
import os
import plotly.graph_objects as go
import tkinter as tk
from tkinter import filedialog
import numpy as np
import statistics
import random
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as fig

def get_entropy(seq, window_size, selected_range, selected_start):
    entropy = []
    tsallis_entropy = []
    renyi_entropy = []
    window_open = selected_start
    window_close = window_open+int(window_size)
    while(window_close < len(seq) and window_close <= selected_range+int(window_size)+int(selected_start)):
        a_count = 0
        g_count = 0
        c_count = 0
        t_count = 0
        window_seq = seq[window_open:window_close]
        for char in window_seq:
            if char == 'A':
                a_count += 1
            else:
                if char == 'G':
                    g_count += 1
                else:
                    if char == 'C':
                        c_count += 1
                    else:
                        if char == 'T':
                            t_count += 1
        entropy.append(shannon(a_count, c_count, g_count, t_count, window_size))
        renyi_entropy.append(renyi(a_count, c_count, g_count, t_count, 0.5))
        tsallis_entropy.append(tsallis(a_count, c_count, g_count, t_count, 0.5))
        window_open += 1
        window_close += 1
    return entropy, renyi_entropy, tsallis_entropy

def get_entropy2(seq, window_size):
    entropy = []
    tsallis_entropy = []
    renyi_entropy = []
    window_open = 0
    window_close = window_open + int(window_size) - 1
    while window_close < len(seq):
        a_count = 0
        g_count = 0
        c_count = 0
        t_count = 0
        window_seq = seq[window_open:window_close]
        for char in window_seq:
            if char == 'A':
                a_count += 1
            else:
                if char == 'G':
                    g_count += 1
                else:
                    if char == 'C':
                        c_count += 1
                    else:
                        if char == 'T':
                            t_count += 1
        entropy.append(round(shannon(a_count, c_count, g_count, t_count, window_size), 2))
        renyi_entropy.append(round(renyi(a_count, c_count, g_count, t_count, 0.5), 2))
        tsallis_entropy.append(round(tsallis(a_count, c_count, g_count, t_count, 0.5), 2))
        window_open += 1
        window_close += 1
    return entropy, renyi_entropy, tsallis_entropy


def shannon(a_count, c_count, g_count, t_count, window_size):
    return -(a_count/window_size * math.log((a_count if a_count != 0 else 1)/window_size, 2)) - \
            (g_count/window_size * math.log((g_count if g_count != 0 else 1)/window_size, 2)) - \
            (t_count/window_size * math.log((t_count if t_count != 0 else 1)/window_size, 2)) - \
            (c_count/window_size * math.log((c_count if c_count != 0 else 1)/window_size, 2))


def renyi(a_count, c_count, g_count, t_count, double):
    window_size = a_count + c_count + g_count + t_count
    entropy = pow(a_count / window_size, double)
    entropy = entropy + pow(c_count / window_size, double)
    entropy = entropy + pow(g_count / window_size, double)
    entropy = entropy + pow(t_count / window_size, double)
    entropy = math.log2(entropy)
    return (1 / (1 - double)) * entropy


def tsallis(a_count, c_count, g_count, t_count, double):
    window_size = a_count + c_count + g_count + t_count
    entropy =  pow(a_count / window_size, double)
    entropy = entropy + pow(c_count / window_size, double)
    entropy = entropy + pow(g_count / window_size, double)
    entropy = entropy + pow(t_count / window_size, double)
    entropy = 1 - entropy
    return (1 / (double - 1)) * entropy


def file_save(f, entropies, renyis, tsalliss, save):
    os.chdir(save)
    with open(f + '.csv', 'w', newline='') as csv_file:
        fieldnames = ['id', 'shannon', 'renyi', 'tsallis']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for index in range(0, len(entropies)):
            writer.writerow({'id': index, 'shannon': entropies[index],
                             "renyi": renyis[index], "tsallis": tsalliss[index]})




def graphTwo(entropies, renyis, tsalliss, e, r, t, names, seq_start, seq_end, self=None):

    global listofGraph
    listofGraph = entropies, renyis, tsalliss, e, r, t, names, seq_start, seq_end


listofGraph = None

def getGraph():
    global listofGraph
    return listofGraph





def similarity(entropies, seq_length, names, file_name):
    outer_list = []
    inner_list = []
    for region1 in range(len(entropies)):
        for region2 in range(len(entropies)):
            if region1 == region2:
                result = 0.0
            elif region2 < region1:
                result = outer_list[region2][region1 + 1]
            else:
                result = walk(entropies[region1], entropies[region2], seq_length) / seq_length
            if len(inner_list) == 0:
                name = names.pop(0)
                inner_list.append(name)
                names.append(name)
            inner_list.append(round(result, 2))
        outer_list.append(inner_list)
        inner_list = []
    saving_files_list = [["names"] + names]
    for index in outer_list:
        saving_files_list.append(index)
    similarity_save(f=file_name, data_list=saving_files_list)
    # TODO make it return entire list later for specific test
    return outer_list


def similarity_save(f, data_list):
    with open(f + ".csv", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data_list)
    f.close()

def walk(list1, list2, window):
    result = -1
    for incline in range(0, len(list1) + len(list2) - 2 * window + 1):
        if incline < len(list1) - window + 1:
            temp = goParallel(list1[len(list1) - window - incline:len(list1)], list2, window)
        else:
            temp = goParallel(list1, list2[incline - len(list1) + window:len(list2)], window)
        if not (temp is None or result > temp or result < -1):
            result = temp
    return result


def goParallel(list1, list2, window):
    if len(list1) < window or len(list2) < window:
        return
    temp = 0
    for i in range(window):
        temp += abs(list1[i] - list2[i])
    temp2 = temp
    last = min(len(list1), len(list2))
    for j in range(window, last):
        temp -= abs(list1[j - window] - list2[j - window])
        temp += abs(list1[j] - list2[j])
        temp2 = min(temp2, temp)
    return temp2


def select(str):
    return str[0] == 'y', str[1] == 'y', str[2] == 'y'


openFile = None
isOpenFile = False


def openFiles():
    names = []
    root = tk.Tk()
    root.withdraw()
    global openFile
    openFile = filedialog.askdirectory(title="open files")
    if openFile:

        os.chdir(openFile)
        for f in os.listdir(openFile):
            os.chdir(openFile)
            filename = open(os.path.abspath(f), 'r')
            if not f.endswith(".fa") and not f.endswith(".fasta"):
                continue
            i = 0
            seq = ''
            for x in filename:
                if x[0] == '>':
                    continue
                else:
                    seq += x.rstrip()
            filename.close()

            names.append(f)
            global isOpenFile
        isOpenFile = True

    return names


def saveFile():
    if savef == []:
        return False
    root = tk.Tk()
    root.withdraw()
    save = filedialog.askdirectory(title="save directory")
    if save:
        for i in range(len(savef)):
            print(savef[i])
            file_save(savef[i], saveEntropy[i], saveRenyis[i], saveTsalliss[i], save)


savef = []
saveEntropy = []
saveRenyis = []
saveTsalliss = []





def tempSave(f, entropies, renyis, tsalliss, save):
    return f, entropies, renyis, tsalliss, save




def classify(matrix, names):
    count = [1]
    symbols = [names[0][0]]
    #count the amount of each type
    for index in range(1, len(names)):
        if names[index][0] == names[index-1][0]:
            count[-1] += 1
        else:
            count.append(1)
            symbols.append(names[index][0])

    new_matrix = []
    #create all possibilites of symbols
    for i in range(len(symbols)):
        for j in range(i, len(symbols)):
            new_matrix.append(f"{symbols[i]}-{symbols[j]}")
    symbols = new_matrix.copy()
    for i in range(len(new_matrix)):
        new_matrix[i] = []
    for i in range(len(names)):
        for j in range(i+1, len(names)):
            for k in range(len(new_matrix)):
                if matrix[i][0][0] == symbols[k][0] and names[j][0] == symbols[k][2]:
                    new_matrix[k].append(matrix[i][j+1])
                    break
    for i in range(len(new_matrix)):
        if not new_matrix[i]:
            new_matrix[i].append(0.0)
    return new_matrix, symbols


def bootstrap(matrix):
    mean_value = []
    for i in range(1000):
        list3 = []
        for i in range(0, len(matrix)):
            list3.append(random.choice(matrix))
        mean_value.append(sum(list3) / len(list3))
    three_values(mean_value, "bootstrap")


def three_values(mean_value, symbols):
    mean = statistics.mean(mean_value)
    if len(mean_value) < 2 and len(mean_value) != 0:
        mean_value.append(mean_value[0])
    elif len(mean_value) == 0:
        print("can't handle empty list of comparison",symbols)
        return
    standard_deviation = statistics.stdev(mean_value)
    print(symbols, round(mean - standard_deviation * 2, 3), mean, round(mean + standard_deviation * 2, 3))
    print("-----------------")




def applySimilarity(window_size ,btnList):
    shannon_list = []
    renyi_list = []
    tsallis_list = []
    names = []

    if isOpenFile == False:
        return False


    checked = 0
    btnCheck = 0
    openFile
    os.chdir(openFile)
    for f in os.listdir(openFile):
        os.chdir(openFile)
        filename = open(os.path.abspath(f), 'r')
        if not f.endswith(".fa") and not f.endswith(".fasta"):
            continue
        i = 0
        seq = ''
        for x in filename:
            if x[0] == '>':
                continue
            else:
                seq += x.rstrip()
        filename.close()
        if len(seq) < window_size:
            continue
        if btnList[checked].isChecked():
            entropies, renyis, tsalliss = get_entropy2(seq, window_size)
            shannon_list.append(entropies)
            renyi_list.append(renyis)
            tsallis_list.append(tsalliss)
            names.append(f)
            btnCheck = btnCheck + 1
        checked = checked + 1

    if btnCheck < 2 :
        return False
    print("bootstrapping+bin")
    matrix = similarity(shannon_list, window_size, names, "shannon_similarity")
    matrix, comparison = classify(matrix, names)
    copy_comparison = comparison.copy()
    all_values = []
    for i in range(len(matrix)):
        all_values.extend(matrix[i])
        three_values(matrix[i], copy_comparison[i])
    bootstrap(all_values)

def main( window_size , e, r, t ):

    if isOpenFile == False:
        return False

    shannon_list = []
    renyi_list = []
    tsallis_list = []
    names = []



    selected_entropies = e,r,t

    e, r, t = select(selected_entropies)
    openFile
    os.chdir(openFile)
    for f in os.listdir(openFile):
        os.chdir(openFile)
        filename = open(os.path.abspath(f), 'r')
        if not f.endswith(".fa") and not f.endswith(".fasta"):
            continue
        i = 0
        seq = ''
        for x in filename:
            if x[0] == '>':
                continue
            else:
                seq += x.rstrip()
        filename.close()
        if len(seq) < window_size:
            continue
        entropies, renyis, tsalliss = get_entropy(seq, window_size, window_size, 0)
        shannon_list.append(entropies)
        renyi_list.append(renyis)
        tsallis_list.append(tsalliss)
        names.append(f)
        print(len(shannon_list))


    global savef, saveEntropy, saveRenyis, saveTsalliss
    savef = names
    saveEntropy = shannon_list
    saveRenyis = renyi_list
    saveTsalliss = tsallis_list
    graphTwo(shannon_list, renyi_list, tsallis_list, e, r, t, names, 0, window_size)
