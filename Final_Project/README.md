# Lab Absorbance Data Cleaner V1.0
## Video Demo: [URL HERE]

## About the Project:
As a Biochemistry student I have often need to take absorbance readings using a spectrophotometer. After collecting the data I also have to clean it, calculate the means and standard deviations, perform statistical tests, create figures... Doing this manually can be repetitive and time-consuming, which is why I'm creating a simple program that will allow me to automate some of this process.

This is the first Version of my Lab Data Cleaner (LADC). This version is designed to take absorbance data in the form of a CSV file, remove invalid absorbance values, calculate summary statistics, create a simple bar chart, perform a t-test and save the results.

### How it Works:
The program is split into five main functions, which are called from main():

1. load_data()
The user is asked for the name of a CSV file, the function opens the file using the csv module, specifically csv.DictReader and returns the data as a list of dictionaries.
If the file cannot be found then the program catches the FileNotFoundError, dislays an error message and the user is again asked to enter a file name.

2. clean_data()
The CSV data (stored as a list of dictionaries) is passed to clean_data(). This function atempts to convert each absorbance value from a string into a float. If a value cannot be converted, the row is skipped and thus 'cleaned' from the data. The remaining rows are then returned as a list.

3. summarise_data()
The cleaned data is then grouped according to the 'group' column (e.g control, sample, treatment...) and for each group the program calculates: 
* The number of measurements, n
* The mean absorbance, mean
* The standard deviation, stdev

The results are then stored in a dictionary which is then passed to the plotting and statistics functions.

4. Plot_Summary()
If the user selects 'Plot' from the menu, the summary data is used to create a bar chart using matplotlib. The height of each bar represents the mean absorbance and the error bars represent the standard deviation. The resulting figurre is returned so that it can later be saved.

5. Run_stats()
If the user selects Stats, the mean, standard deviation and the nummber of observations from the two groups are passed to scipy.stats.ttest_ind_from_stats(). This performs an independent samples t-test and returns the test statistic and p-value.

#### User Menu

after the data has been loaded, cleaned and summarised, the user is presented with four options:
1. Plot - Creates and displats a bar chart of mean absorbances.
2. Stats - Performs an independent samples t-test between the two groups.
3. Save - Saves the generated results
4. Exit - closes the program

If an invalid menu option is entered, the user is asked to try again. 

#### Saving Results

The Save option creates a new folder insides the Save directory using a name provided by the user, if their is no Save directory, one will be created with the new folder created inside.

The program saves the following:
* The generated bar chart as 'plot.png'
* The t-test results, cleaned data and summary statistics as 'data.json'

The JSON file allows the results to be stored in a structured format that can be accessed again later.


## Assumptions:
As this is the first version of the program and the first project I have ever undertaken, there are some limitations, so assumptions have been made about the input data and analysis:
* The statistical function currently expects exactly two groups, and each group needs at least two measurements in oder to calculate a standard deviation
* The input CSV is expected to contain the columns: sample_id, group and absorbance
* The CSV is assumed to be a clean, header-first file with no additional metadata rows or instrument-specific formatting.

## Future Direction:
In the future i'd like to develop this program further by implementing several features:
* Standard Curves — Allow samples with known concentration to be used to generate a standard curve and calculate the concentration of unknown samples using the Beer-Lambert law. slope, intercept, R^2, equation and calculation of unknown concentrations could also be reported.
* Customizable plots — Allow for user driven design choices such as choosing between bar, line, scatter as opposed to having a single hardcoded chart type.
* Header name normalization — recognise any variations such as Abs, OD and Absorbance and map them to a standard column name
* More than two groups (ANOVA) — extend the statistical analysis to support more than two groups using ANOVA. THis would allow additional groups such as blanks or positive/negative controls to be included.
* More flexible CSV handling — Support instrumental files containing metadata rows, multiple wavelength columns, or other common formatting variations.

and so much more from better data cleaning, with a report on missing or non numeric values - a why to each removed sample, Detect outlier absorbance data, blank correction ( corrected = sample - blank ), expand the amount of statistical tests like: independent t-test, paired t-test, Welch's t-test, one-way ANOVA, correlation, linear regression... The list is evergrowing and what was initially just a data cleaner has quickly expanded into a project that I will work on after submission.
