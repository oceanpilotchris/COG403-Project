# import libraries.

import numpy as np
import scipy as cp
import csv
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# open csv file of the LIWC results.
csv_file = open("result.csv", "r", encoding='utf-8')

# All the measures provided by LIWC.
measures = ['year', 'WC', 'Analytic', 'Clout', 'Authentic', 'Tone', 'WPS', 'Sixltr', 'Dic', 'function', 'pronoun', 'ppron', 'i', 'we', 'you', 'shehe', 'they', 'ipron', 'article', 'prep', 'auxverb', 'adverb', 'conj', 'negate', 'verb', 'adj', 'compare', 'interrog', 'number', 'quant', 'affect', 'posemo', 'negemo', 'anx', 'anger', 'sad', 'social', 'family', 'friend', 'female', 'male', 'cogproc', 'insight', 'cause', 'discrep', 'tentat', 'certain', 'differ', 'percept', 'see', 'hear', 'feel', 'bio', 'body', 'health', 'sexual', 'ingest', 'drives', 'affiliation', 'achieve', 'power', 'reward', 'risk', 'focuspast', 'focuspresent', 'focusfuture', 'relativ', 'motion', 'space', 'time', 'work', 'leisure', 'home', 'money', 'relig', 'death', 'informal', 'swear', 'netspeak', 'assent', 'nonflu', 'filler', 'AllPunc', 'Period', 'Comma', 'Colon', 'SemiC', 'QMark', 'Exclam', 'Dash', 'Quote', 'Apostro', 'Parenth', 'OtherP']

# Create a dictionary where the keys are the measures.
measure_dict = {}

for measure in measures:
    measure_dict[measure] = []

# Insert the values into the dictionary
csv_reader = csv.DictReader(csv_file)
for row in csv_reader:
    for measure in measures:
        measure_dict[measure].append(float(row[measure]))

# input the stats of the any mental illness (AMI) rate from NIMH in 2008-2019 for adults
# in the 4 age groups: 18 and older, 18-25, 26-49, and 50 and older.

year = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
ami_18_older = [17.7, 18.1, 18.1, 17.8, 18.6, 18.5, 18.1, 17.9, 18.3, 18.9, 19.1, 20.6]
ami_18_25 = [18.5, 18.0, 18.1, 18.5, 19.6, 19.4, 20.1, 21.7, 22.1, 25.8, 26.3, 29.4]
ami_26_49 = [20.7, 21.6, 20.9, 20.3, 21.2, 21.5, 20.4, 20.9, 21.1, 22.2, 22.5, 25.0]
ami_50_older = [14.1, 14.5, 15.1, 15.0, 15.8, 15.3, 15.4, 14.0, 14.5, 13.8, 14.0, 14.1]

# Calculate the correlation between lyrics measures and mental illness index (18_older and 18 to 25),
# and remove the "year" key.

corr_18_older = {}
for measure in measures:
    corr_value = cp.stats.pearsonr(measure_dict[measure], ami_18_older)
    corr_18_older[measure] = [corr_value]
corr_18_older.pop("year", None)

corr_18_25 = {}
for measure in measures:
    corr_value = cp.stats.pearsonr(measure_dict[measure], ami_18_25)
    corr_18_25[measure] = [corr_value]
corr_18_25.pop("year", None)

# Only keep the measures with strong correlations with mental health
# and divided them by strong positive or strong negative corr

posicorr_18_older = {}
negacorr_18_older = {}
for key in corr_18_older:
    if corr_18_older[key][0][0] >= 0.7:
        posicorr_18_older[key] = corr_18_older[key]
    if corr_18_older[key][0][0] <= -0.7:
        negacorr_18_older[key] = corr_18_older[key]

posicorr_18_25 = {}
negacorr_18_25 = {}
for key in corr_18_25:
    if corr_18_25[key][0][0] >= 0.7:
        posicorr_18_25[key] = corr_18_25[key]
    if corr_18_25[key][0][0] <= -0.7:
        negacorr_18_25[key] = corr_18_25[key]

print(len(posicorr_18_older))
print(len(negacorr_18_older))
print(len(posicorr_18_25))
print(len(negacorr_18_25))

#



fig = go.Figure(data=[go.Table(header=dict(values=['Measure', 'r']),
                               cells=dict(values=[[100, 90, 80, 90], [95, 85, 75, 95]]))
                      ])
fig.show()

plt.plot(measure_dict["year"], measure_dict["Comma"])
# plt.xticks(np.arange(min(x), max(x)+1, 1.0))
# plt.xticks(np.arange(min(x), max(x)+1, 1.0))
#plt.show()



