import matplotlib.pyplot as plt
import numpy as np

def main(): # bar chart
    # need to import the data
    results = {'control': {'n': 2, 'mean': 0.405, 'stdev': 0.009899494936611635}, 'treatment': {'n': 2, 'mean': 0.6865, 'stdev': 0.021920310216782913}}

    names = list(results.keys())
    means = [data['mean'] for data in results.values()]
    stdevs = [data['stdev'] for data in results.values()]

    plt.figure(figsize=(6,4))

    plt.bar(names, means, yerr=stdevs, capsize=4)

    plt.title('Mean Absorbances')
    plt.xlabel('Absorbance (AU)')
    plt.ylabel('Samples')

    plt.show()

main()