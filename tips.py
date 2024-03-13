import seaborn as sns
import pandas as pd
import numpy as np
from scipy import stats
import plotly.graph_objects as go
import plotly.express as px

df = sns.load_dataset('tips')



#Unsupervised Data

#Contenuous - total_bill, tip
#Category - sex, smoker, day, time,	size

corr = df.corr()

#             two sample test  
#total_bill, tip 	   - H0 is rejected

#             chi2 test
#total_bill, sex	    - H0 is rejected
#total_bill, smoker   - H0 is accepted
#total_bill, day     - H0 is rejected
#total_bill, time	    - H0 is rejected
#total_bill, size    - H0 is rejected
#tip, sex,	          - H0 is accepted
#tip, smoker          - H0 is accepted
#tip, day            - H0 is accepted
#tip, time	          - H0 is accepted
#tip, size            - H0 is rejected

#            Anova
#sex, smoker          - H0 is accepted
#sex, day              - H0 is rejected
#sex, time	          - H0 is rejected
#sex, size           - H0 is accepted
#day, time	        - H0 is rejected
#day, size	         - H0 is rejected
#time, size	         - H0 is rejected

#Two sample ttest for continuous VS continuous data columns
#total_bill,	tip
for i in range(20):
  sample1 = df.total_bill.sample(frac=0.04)
  sample2 = df.tip.sample(frac=0.04)

  t_test, p_value = stats.ttest_ind(sample1, sample2)

  if p_value > 0.5:
    print("H0 is accepted")
  else:
    print('H0 is rejected')

Output Result "H0 is rejected"


#Chi-2 Test for category VS category
data = pd.crosstab(df["sex"], df["smoker"])
observed_values = data.values
result = stats.chi2_contingency(observed_values)


#sex, smoker - H0 is accepted

data = pd.crosstab(df["sex"], df["smoker"])
observed_values = data.values
chi2_stat, p_value, _, _= stats.chi2_contingency(observed_values)

if p_value > 0.05:
  print("H0 is accepted")
else:
  print("H0 is rejected")


#sex, day

data = pd.crosstab(df["sex"], df["day"])
observed_values = data.values
chi2_stat, p_value, _, _= stats.chi2_contingency(observed_values)

if p_value > 0.05:
  print("H0 is accepted")
else:
  print("H0 is rejected")


#sex, time

data = pd.crosstab(df["sex"], df["time"])
observed_values = data.values
chi2_stat, p_value, _, _= stats.chi2_contingency(observed_values)

if p_value > 0.05:
  print("H0 is accepted")
else:
  print("H0 is rejected")

#sex, size

data = pd.crosstab(df["sex"], df["size"])
observed_values = data.values
chi2_stat, p_value, _, _= stats.chi2_contingency(observed_values)

if p_value > 0.05:
  print("H0 is accepted")
else:
  print("H0 is rejected")

#day, time

data = pd.crosstab(df["day"], df["time"])
observed_values = data.values
chi2_stat, p_value, _, _= stats.chi2_contingency(observed_values)

if p_value > 0.05:
  print("H0 is accepted")
else:
  print("H0 is rejected")

#day, size

data = pd.crosstab(df["day"], df["size"])
observed_values = data.values
chi2_stat, p_value, _, _= stats.chi2_contingency(observed_values)

if p_value > 0.05:
  print("H0 is accepted")
else:
  print("H0 is rejected")

#time, size

data = pd.crosstab(df["time"], df["size"])
observed_values = data.values
chi2_stat, p_value, _, _= stats.chi2_contingency(observed_values)

if p_value > 0.05:
  print("H0 is accepted")
else:
  print("H0 is rejected")

#total_bill, sex
group = df['sex'].unique()
data = {}
for i in group:
  data[i]=df["total_bill"][df["sex"]==i]

f_value, p_value = stats.f_oneway( data['Male'], data['Female'] )
print(f_value, p_value)
if p_value<0.05:
  print("H0 - Null hypothesis is rejected which means no relationship exists")
else:
  print("Ha - Null hypothesis is accepted which means relationship exists")


#total_bill, smoker
group = df['smoker'].unique()
data = {}
for i in group:
  data[i]=df["total_bill"][df["smoker"]==i]

f_value, p_value = stats.f_oneway( data['No'], data['Yes'] )
print(f_value, p_value)
if p_value<0.05:
  print("H0 - Null hypothesis is rejected which means no relationship exists")
else:
  print("Ha - Null hypothesis is accepted which means relationship exists")

#total_bill, day
group = df['day'].unique()
data = {}
for i in group:
  data[i]=df["total_bill"][df["day"]==i]

f_value, p_value = stats.f_oneway(data['Thur'], data['Fri'], data['Sat'], data['Sun'] )
print(f_value, p_value)
if p_value<0.05:
  print("H0 - Null hypothesis is rejected which means no relationship exists")
else:
  print("Ha - Null hypothesis is accepted which means relationship exists")

#total_bill, time
group = df['time'].unique()
data = {}
for i in group:
  data[i]=df["total_bill"][df["time"]==i]

f_value, p_value = stats.f_oneway(data['Lunch'], data['Dinner'] )
print(f_value, p_value)
if p_value<0.05:
  print("H0 - Null hypothesis is rejected which means no relationship exists")
else:
  print("Ha - Null hypothesis is accepted which means relationship exists")


#total_bill, size
group = df['size'].unique()
data = {}
for i in group:
  data[i]=df["total_bill"][df["size"]==i]

f_value, p_value = stats.f_oneway(data[1], data[2], data[3], data[4], data[5], data[6] )
print(f_value, p_value)
if p_value<0.05:
  print("H0 - Null hypothesis is rejected which means no relationship exists")
else:
  print("Ha - Null hypothesis is accepted which means relationship exists")

#tip, sex,
group = df['sex'].unique()
data = {}
for i in group:
  data[i]=df["tip"][df["sex"]==i]

f_value, p_value = stats.f_oneway(data['Male'], data['Female'] )
print(f_value, p_value)
if p_value<0.05:
  print("H0 - Null hypothesis is rejected which means no relationship exists")
else:
  print("Ha - Null hypothesis is accepted which means relationship exists")

#tip, smoker
group = df['smoker'].unique()
data = {}
for i in group:
  data[i]=df["tip"][df["smoker"]==i]

f_value, p_value = stats.f_oneway(data['No'], data['Yes'] )
print(f_value, p_value)
if p_value<0.05:
  print("H0 - Null hypothesis is rejected which means no relationship exists")
else:
  print("Ha - Null hypothesis is accepted which means relationship exists")

#tip, day
group = df['day'].unique()
data = {}
for i in group:
  data[i]=df["tip"][df["day"]==i]

f_value, p_value = stats.f_oneway(data['Thur'], data['Fri'], data['Sat'], data['Sun'] )
print(f_value, p_value)
if p_value<0.05:
  print("H0 - Null hypothesis is rejected which means no relationship exists")
else:
  print("Ha - Null hypothesis is accepted which means relationship exists")


#tip, time
group = df['time'].unique()
data = {}
for i in group:
  data[i]=df["tip"][df["time"]==i]

f_value, p_value = stats.f_oneway(data['Lunch'], data['Dinner'] )
print(f_value, p_value)
if p_value<0.05:
  print("H0 - Null hypothesis is rejected which means no relationship exists")
else:
  print("Ha - Null hypothesis is accepted which means relationship exists")


#tip, size
group = df['size'].unique()
data = {}
for i in group:
  data[i]=df["tip"][df["size"]==i]

f_value, p_value = stats.f_oneway(data[1], data[2], data[3], data[4], data[5], data[6] )
print(f_value, p_value)
if p_value<0.05:
  print("H0 - Null hypothesis is rejected which means no relationship exists")
else:
  print("Ha - Null hypothesis is accepted which means relationship exists")




#tip, day
fig = px.bar(df, x = 'day',
                 y = 'tip',
                 title = 'Day vs Tip'
                )
fig.show()
