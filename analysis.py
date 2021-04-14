# import numpy library and sklearn library
import numpy as np
import scipy as cp
import csv
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# open csv file of the LIWC results.
csv_file = open("result.csv", "r", encoding='utf-8')
# read csv file as a dictionaries, you can access each dictionary by iterating
# through them.

measures = ['year', 'WC', 'Analytic', 'Clout', 'Authentic', 'Tone', 'WPS', 'Sixltr', 'Dic', 'function', 'pronoun', 'ppron', 'i', 'we', 'you', 'shehe', 'they', 'ipron', 'article', 'prep', 'auxverb', 'adverb', 'conj', 'negate', 'verb', 'adj', 'compare', 'interrog', 'number', 'quant', 'affect', 'posemo', 'negemo', 'anx', 'anger', 'sad', 'social', 'family', 'friend', 'female', 'male', 'cogproc', 'insight', 'cause', 'discrep', 'tentat', 'certain', 'differ', 'percept', 'see', 'hear', 'feel', 'bio', 'body', 'health', 'sexual', 'ingest', 'drives', 'affiliation', 'achieve', 'power', 'reward', 'risk', 'focuspast', 'focuspresent', 'focusfuture', 'relativ', 'motion', 'space', 'time', 'work', 'leisure', 'home', 'money', 'relig', 'death', 'informal', 'swear', 'netspeak', 'assent', 'nonflu', 'filler', 'AllPunc', 'Period', 'Comma', 'Colon', 'SemiC', 'QMark', 'Exclam', 'Dash', 'Quote', 'Apostro', 'Parenth', 'OtherP']

measure_dict = {}

for measure in measures:
    measure_dict[measure] = []

csv_reader = csv.DictReader(csv_file)
for row in csv_reader:
    for measure in measures:
        measure_dict[measure].append(float(row[measure]))

plt.plot(measure_dict["year"], measure_dict["Comma"])
# plt.xticks(np.arange(min(x), max(x)+1, 1.0))
# plt.xticks(np.arange(min(x), max(x)+1, 1.0))
#plt.show()



# find the desired statistics of the anuual mental illness index of the US from
# NIMH
#https://www.samhsa.gov/data/sites/default/files/reports/rpt29393/2019NSDUHFFRPDFWHTML/2019NSDUHFFR1PDFW090120.pdf
#P44

# input the stats of the any mental illness (AMI) rate from 2008-2019 for adults
# in the 4 age groups: 18 and older, 18-25, 26-49, and 50 and older.

year = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
ami_18_older = [17.7, 18.1, 18.1, 17.8, 18.6, 18.5, 18.1, 17.9, 18.3, 18.9, 19.1, 20.6]
ami_18_25 = [18.5, 18.0, 18.1, 18.5, 19.6, 19.4, 20.1, 21.7, 22.1, 25.8, 26.3, 29.4]
ami_26_49 = [20.7, 21.6, 20.9, 20.3, 21.2, 21.5, 20.4, 20.9, 21.1, 22.2, 22.5, 25.0]
ami_50_older = [14.1, 14.5, 15.1, 15.0, 15.8, 15.3, 15.4, 14.0, 14.5, 13.8, 14.0, 14.1]

cc1 = np.corrcoef(measure_dict["Clout"], ami_18_older)
print(cc1)

cc2 = np.corrcoef(measure_dict["Dash"], ami_18_older)
#print(cc2)

cc3 = cp.stats.pearsonr(measure_dict["posemo"], ami_18_older)
print(cc3)


