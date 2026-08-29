import os
import csv
import json
from pyfiglet import Figlet
import statistics as sts
import matplotlib.pyplot as plt
from scipy import stats


def main():
    f = Figlet(font='banner3-D')
    print(f.renderText('Lab Data Cleaner'))

    # bring all functions together
    while True:
        try:
            l_file = load_data(input("File name: "))
            break
        except FileNotFoundError:
            print("File not found. Please try again.")
            continue
    
    c_file = clean_data(l_file)
    s_file = summarise_data(c_file)
    fig = None
    result = None

    while True:
        menu = input("""\nWelcome to the LADC v1.0 Please choose the following:

        1. Plot

        2. Stats

        3. Save

        4. Exit
        \nChoice: """).strip()

    
        if menu == "1":
            fig = plot_summary(s_file)

        elif menu == "2":
            result = run_stats(s_file)

        elif menu == "3":
            save_progress(fig, result, c_file, s_file)

        elif menu == "4":
            print("Thank you for using my Program")
            break

        else:
            print("\n", "-" * 40, "\n         Invalid Choice Try Again","\n", "-" * 40)


def load_data(name): # reads the csv - returns a list of dicts
    
    with open(name, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

def clean_data(loaded_file): # removes rows containing non-numeric absorbances - converts absorbances to floats.

    cleaned = []
    for row in loaded_file:
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

    
def plot_summary(results): # bar chart # needs to save
    # need to import the data
    names = list(results.keys())
    means = [data['mean'] for data in results.values()]
    stdevs = [data['stdev'] for data in results.values()]

    fig = plt.figure(figsize=(6,4))

    plt.bar(names, means, yerr=stdevs, capsize=4)

    plt.title('Mean Absorbances')
    plt.xlabel('Samples')
    plt.ylabel('Absorbance (AU)')

    plt.show()

    return fig

def run_stats(results):

    nobs1, nobs2 = [data['n'] for data in results.values()]
    mean1, mean2 = [data['mean'] for data in results.values()]
    std1, std2 = [data['stdev'] for data in results.values()]

    result = stats.ttest_ind_from_stats(mean1, std1, nobs1, mean2, std2, nobs2, equal_var=False)
    print(result)
    return result

def save_progress(fig, res, clean, summ):
    # look at file I/O  ??
    # stores each csv with its plot and t test if chosen.
    yes = ['y', 'Y', 'yes', 'Yes']
    no = ['n', 'N', 'no', 'No']

    while True:
        decision = input("""\nWould you like to save:
        (Y) yes
        (N) no    
        input: """)
        
        if decision in yes:

            save_folder = './Save'
            data_folder = input("Save as: ")
            full_path = os.path.join(save_folder, data_folder)

            if not os.path.exists(full_path):
                os.makedirs(full_path)
            else:
                print("\nThis file already exists\n")
                continue


            fig.savefig(os.path.join(full_path, 'plot.png'))
            with open(os.path.join(full_path, 'data.json'), 'w') as f:
                stat_data = {'statistic': res.statistic, 'pvalue': res.pvalue}
                save_data = {'stats': stat_data, 'cleaned': clean, 'summary': summ}
                json.dump(save_data, f)

            break

        elif decision in no:
            break

        else:
            print("Invalid Choice")
            continue
        


if __name__ == "__main__":
    main()