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

# plotting the correlations and p-values

measure1 = []
value1 = []
for key in posicorr_18_older:
    measure1.append(key)
    if posicorr_18_older[key][0][1] <= 0.01:
        value1.append(str(posicorr_18_older[key][0][0]) + '**')
    elif 0.01 < posicorr_18_older[key][0][1] < 0.05:
        value1.append(str(posicorr_18_older[key][0][0]) + '*')
    else:
        value1.append(str(posicorr_18_older[key][0][0]))

# fig1 = go.Figure(data=[go.Table(header=dict(values=['Measure', 'r']),
#                                cells=dict(values=[measure1, value1]))
#                       ])
# fig1.update_layout(title="Strong Positive Correlations between lyrics preference and mental illness rate of adults aged 18 or older")
# fig1.show()
#
# measure2 = []
# value2 = []
# for key in negacorr_18_older:
#     measure2.append(key)
#     if negacorr_18_older[key][0][1] >= -0.01:
#         value2.append(str(negacorr_18_older[key][0][0]) + '**')
#     elif -0.05 < negacorr_18_older[key][0][1] < -0.01:
#         value2.append(str(negacorr_18_older[key][0][0]) + '*')
#     else:
#         value2.append(str(negacorr_18_older[key][0][0]))
#
# fig2 = go.Figure(data=[go.Table(header=dict(values=['Measure', 'r']),
#                                 cells=dict(values=[measure2, value2]))
#                        ])
# fig2.update_layout(title="Strong Negative Correlations between lyrics preference and mental illness rate of adults aged 18 or older")
# fig2.show()
#
# measure3 = []
# value3 = []
# for key in posicorr_18_25:
#     measure3.append(key)
#     if posicorr_18_25[key][0][1] <= 0.01:
#         value3.append(str(posicorr_18_25[key][0][0]) + '**')
#     elif 0.01 < posicorr_18_25[key][0][1] < 0.05:
#         value3.append(str(posicorr_18_25[key][0][0]) + '*')
#     else:
#         value3.append(str(posicorr_18_25[key][0][0]))
#
# fig3 = go.Figure(data=[go.Table(header=dict(values=['Measure', 'r']),
#                                 cells=dict(values=[measure3, value3]))
#                        ])
# fig3.update_layout(title="Strong Positive Correlations between lyrics preference and mental illness rate of adults aged 18-25")
# fig3.show()
#
# measure4 = []
# value4 = []
# for key in negacorr_18_25:
#     measure4.append(key)
#     if negacorr_18_25[key][0][1] >= -0.01:
#         value4.append(str(negacorr_18_25[key][0][0]) + '**')
#     elif -0.05 < negacorr_18_25[key][0][1] < -0.01:
#         value4.append(str(negacorr_18_25[key][0][0]) + '*')
#     else:
#         value4.append(str(negacorr_18_25[key][0][0]))
#
# fig4 = go.Figure(data=[go.Table(header=dict(values=['Measure', 'r']),
#                                 cells=dict(values=[measure4, value4]))
#                        ])
# fig4.update_layout(title="Strong Negative Correlations between lyrics preference and mental illness rate of adults aged 18-25")
# fig4.show()

# Plot the lyrics measures over time

# plt.plot(measure_dict["year"], measure_dict["Comma"])
# plt.xticks(np.arange(min(x), max(x)+1, 1.0))
# plt.xticks(np.arange(min(x), max(x)+1, 1.0))
#plt.show()

increased_keys = ["negemo", "anger", "friend", "sexual", "informal", "swear", "assent", "money", "netspeak"]
y1 = measure_dict["negemo"]
y2 = measure_dict["anger"]
y3 = measure_dict["friend"]
y4 = measure_dict["sexual"]
y5 = measure_dict["informal"]
y6 = measure_dict["swear"]
y7 = measure_dict["assent"]
y8 = measure_dict["money"]
y9 = measure_dict["netspeak"]

plt.plot(year, y1, "b", label="Negative Emotion")
plt.plot(year, y2, "g", label="Anger")
plt.plot(year, y3, "r", label="Friend")
plt.plot(year, y4, "c", label="Sexual")
plt.plot(year, y5, "m", label="Informal")
plt.plot(year, y6, "y", label="Swear")
plt.plot(year, y7, "k", label="Assent")
plt.plot(year, y8, "b", linestyle="dotted", label="Money")
plt.plot(year, y9, "g", linestyle="dotted", label="Netspeak")
plt.xlabel("Year")
plt.ylabel("Value of Lyrics Semantics Measures")
plt.title('Lyrics Measures that are expected to increase over time')
plt.legend(bbox_to_anchor=(0.8, 1), loc='upper left', fontsize='xx-small')
plt.show()


decreased_keys = ["Clout", "Tone", "compare", "achieve", "Dic", "function", "ipron", "auxverb", "conj", "interrog", "social", "cogproc", "differ", "time"]

y1 = measure_dict["Clout"]
y2 = measure_dict["Tone"]
y3 = measure_dict["compare"]
y4 = measure_dict["achieve"]
y5 = measure_dict["Dic"]
y6 = measure_dict["function"]
y7 = measure_dict["ipron"]
y8 = measure_dict["auxverb"]
y9 = measure_dict["conj"]
y10 = measure_dict["interrog"]
y11 = measure_dict["social"]
y12 = measure_dict["cogproc"]
y13 = measure_dict["differ"]
y14 = measure_dict["time"]

plt.plot(year, y1, "b", label="Clout")
plt.plot(year, y2, "g", label="Tone")
plt.plot(year, y3, "r", label="Compare")
plt.plot(year, y4, "c", label="Achieve")
plt.plot(year, y5, "m", label="Dicionary words")
plt.plot(year, y6, "y", label="Function")
plt.plot(year, y7, "k", label="Impersonal pronouns")
plt.plot(year, y8, "b", linestyle="dotted", label="Auxiliary verbs")
plt.plot(year, y9, "g", linestyle="dotted", label="Conjunction words")
plt.plot(year, y10, "r", linestyle="dotted", label="Interrogatives")
plt.plot(year, y11, "c", linestyle="dotted", label="Social")
plt.plot(year, y12, "m", linestyle="dotted", label="Cognitive processes")
plt.plot(year, y13, "y", linestyle="dotted", label="Differentiation")
plt.plot(year, y14, "k", linestyle="dotted", label="Time")

plt.xlabel("Year")
plt.ylabel("Value of Lyrics Semantics Measures")
plt.title('Lyrics Measures that are expected to decrease over time')
plt.legend(bbox_to_anchor=(0.8, 1), loc='upper left', fontsize='xx-small')
plt.show()
