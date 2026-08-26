import sys
import csv
from pyfiglet import Figlet
import statistics as sts
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def main():
    f = Figlet(font='banner3-D')
    print(f.renderText('Lab Data Cleaner'))

    # bring all functions together
    l_file = load_data()
    c_file = clean_data(l_file)
    s_file = summarise_data(c_file)

    while True:
        menu = input("""\nWelcome to the LADC v1.0 Please choose the following:

        1. Plot

        2. Stats

        3. Skip
        \nChoice: """)

    
        if menu == "1":
            plot_summary(s_file, save_progress())
        elif menu == "2":
            run_stats(s_file, save_progress())
        elif menu == "3":
            save_progress()
        else:
            print("\n", "-" * 40, "\n         Invalid Choice Try Again","\n", "-" * 40)

def load_data(): # reads the csv - returns a list of dicts
    
    while True:
        try:
            with open(input("File name: "), newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                return list(reader)
            
        except FileNotFoundError:
            print("File not found. Please try again.")
            continue

def clean_data(f): # flags missing / non-numeric - 'cleans' it

    cleaned = []
    for row in f:
        try:
            row['absorbance'] = float(row['absorbance']) # converts to a float
            cleaned.append(row)

        except ValueError:
            pass

    return cleaned

def summarise_data(s): # returns a dict where per group it gives the number, its mean and its std dev

    summarised = {} # new dictionary

    for row in s:
        summarised.setdefault(row['group'], []) # creating new groups if different one found
        summarised[row['group']].append(row['absorbance']) # absorbances now added to each group

    for group, value in summarised.items(): # group here is either control / sample   # value is the absorbances measured
        n = len(summarised[group]) # number of values
        m = sts.mean(value)        # mean of values         
        std = sts.stdev(value)     # standard deviation of values

        summarised[group] = {'n': n, 'mean': m, 'stdev': std} # groups should now read as such with above calculations

    return summarised

    
def plot_summary(results, save): # bar chart
    # need to import the data
    names = list(results.keys())
    means = [data['mean'] for data in results.values()]
    stdevs = [data['stdev'] for data in results.values()]
    # and make the bar chart
    plt.figure(figsize=(6,4))

    plt.bar(names, means, yerr=stdevs, capsize=4)

    plt.title('Mean Absorbances')
    plt.xlabel('Samples')
    plt.ylabel('Absorbance (AU)')

    plt.show()


def run_stats():
    # t-test

def save_progress():
    # look at file I/O / using pickle ??
    # stores each csv with its plot and t test if chosen.


main()