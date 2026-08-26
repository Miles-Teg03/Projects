# Absorbance Data Cleaner V1.0
#### Video Demo: [URL HERE]

#### Description:
I'm creating a program that will allow me to clean data gathered using a spectrophotometer in a wet lab setting. 
in its first version, this program has the following capabilities:
* load and clean csv file containing data
* calculate the mean and standard deviation of two groups (control and sample)
* optionally perform a t-test and/or create a figure 
* save any progress (NOTE: will likely use pickle )

#### Assumptions:
key names within csv file are exactly :  sample_id, group, absorbance
there are only two groups : a control and a sample (in my example this is called treatment)

#### Future Direction:
In the future i'd like to extend this program to:
* Create a standard curve of samples with known concentration + Beer-Lambert law to find concentration of a sample
* Customizable chart type (user choosing bar/line/scatter) — plot_summary() uses one hardcoded chart type chosen at design time, not a runtime option.
* Header/column-name normalization — no matching Abs/OD/Absorbance variants to a canonical name; assumes the input CSV has your exact header row (sample_id,group,absorbance).
More than two groups (ANOVA) — run_stats() assumes exactly two groups; a third group (e.g. blank, positive/negative control) isn't handled.
Messy real-world exports — no handling of metadata rows above the header, multiple wavelength columns, or non-tabular instrument quirks; assumes a clean, header-first CSV.
#### To Do: 
* def summarise_data
* def plot_summary
* def run_stats
* def save_progress