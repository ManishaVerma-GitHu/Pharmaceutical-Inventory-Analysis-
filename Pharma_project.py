# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 16:36:05 2024

@author: Manisha
"""

import pandas as pd
import numpy as np

df = pd.read_csv(r'C:/Users/Manisha/Documents/Project3_dataset.csv')

print(df.info())

############## First/ Second/ Third/ Fourth  Moment Business Decision ############

df['Qty in Un. of Entry'] = pd.to_numeric(df['Qty in Un. of Entry'], errors = 'coerce')

df['Qty in Un. of Entry'].mean()
df['Qty in Un. of Entry'].median()
df['Qty in Un. of Entry'].mode()
df['Qty in Un. of Entry'].std()
df['Qty in Un. of Entry'].var()
df['Qty in Un. of Entry'].max() - df['Qty in Un. of Entry'].min()
df['Qty in Un. of Entry'].skew()
df['Qty in Un. of Entry'].kurt()


##################### GRAPHICAL REPRESENTATION ###############################

########################## HISTOGRAM ###############################
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
plt.hist(df['Qty in Un. of Entry'],bins = 20 )
plt.title("Qty in Un. of Entry")
plt.tight_layout()
plt.show()

######################## Q-Q PLOT ##############

import seaborn as sns
import scipy.stats as stats


data = np.random.normal(loc=0, scale=1, size=1000)

plt.figure(figsize=(8, 6))
stats.probplot(df['Qty in Un. of Entry'], dist="norm", plot=plt)
plt.title("Q-Q Plot", fontsize=16)
plt.grid(True)
plt.show()

################### DENSITY PLOT ##################
plt.figure(figsize=(8, 6))
sns.kdeplot(df['Qty in Un. of Entry'], fill=True, color='blue', alpha=0.5)
plt.title("Density Plot", fontsize=16)
plt.xlabel("Data", fontsize=12)
plt.ylabel("Density", fontsize=12)
plt.grid(True)
plt.show()

############## DUPLICATES ##############

df.drop_duplicates (keep = 'first')
print(df)

########### MISSING VALUES ###########

missing_values = df['Qty in Un. of Entry'].isnull().any()
print("missing values present in:", missing_values)

################# OUTLIER ##################

import seaborn as sns

sns.boxplot(df['Qty in Un. of Entry'])
IQR = df['Qty in Un. of Entry'].quantile(0.75) - df['Qty in Un. of Entry'].quantile(0.25)
lower_limit = df['Qty in Un. of Entry'].quantile(0.25) - (IQR * 1.5)
upper_limit = df['Qty in Un. of Entry'].quantile(0.75) + (IQR * 1.5)

#Replace the outliers by the maximum and minimum limit
replace_val = pd.DataFrame(np.where(df['Qty in Un. of Entry'] > upper_limit, upper_limit, np.where(df['Qty in Un. of Entry'] < lower_limit, lower_limit, df['Qty in Un. of Entry'])))
sns.boxplot(replace_val)

#################### NORMALIZATION ########################

from sklearn.preprocessing import MinMaxScaler
###data = pd.read_excel('data.xlsx')
scaler = MinMaxScaler()
df['Qty in Un. of Entry'] = scaler.fit_transform(df[['Qty in Un. of Entry']])
print(df)

############### TRANSFORMATION ##########################
df['Value_log'] = np.log(df['Qty in Un. of Entry'])
print(df)



############## First/ Second/ Third/ Fourth  Moment Business Decision ############

df['Qty in OPUn'] = pd.to_numeric(df['Qty in OPUn'], errors = 'coerce')

df['Qty in OPUn'].mean()
df['Qty in OPUn'].median()
df['Qty in OPUn'].mode()
df['Qty in OPUn'].std()
df['Qty in OPUn'].var()
df['Qty in OPUn'].max() - df['Qty in OPUn'].min()
df['Qty in OPUn'].skew()
df['Qty in OPUn'].kurt()

################ GRAPHICAL REPRESENTATION ################

import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
plt.hist(df['Qty in OPUn'],bins = 20 )
plt.title("Qty in OPUn")
plt.tight_layout()
plt.show()

####################### Q-Q PLOT ##############

import seaborn as sns
import scipy.stats as stats


data = np.random.normal(loc=0, scale=1, size=1000)

plt.figure(figsize=(8, 6))
stats.probplot(df['Qty in OPUn'], dist="norm", plot=plt)
plt.title("Q-Q Plot", fontsize=16)
plt.grid(True)
plt.show()

################### DENSITY PLOT ##################
plt.figure(figsize=(8, 6))
sns.kdeplot(df['Qty in OPUn'], fill=True, color='blue', alpha=0.5)
plt.title("Density Plot", fontsize=16)
plt.xlabel("Data", fontsize=12)
plt.ylabel("Density", fontsize=12)
plt.grid(True)
plt.show()

############## DUPLICATES ##############

df.drop_duplicates (keep = 'first')
print(df)

########### MISSING VALUES ###########

missing_values = df['Qty in OPUn'].isnull().any()
print("missing values present in:", missing_values)


################# OUTLIER ##################

import seaborn as sns

sns.boxplot(df['Qty in OPUn'])
IQR = df['Qty in OPUn'].quantile(0.75) - df['Qty in OPUn'].quantile(0.25)
lower_limit = df['Qty in OPUn'].quantile(0.25) - (IQR * 1.5)
upper_limit = df['Qty in OPUn'].quantile(0.75) + (IQR * 1.5)

#Replace the outliers by the maximum and minimum limit
replace_val = pd.DataFrame(np.where(df['Qty in OPUn'] > upper_limit, upper_limit, np.where(df['Qty in OPUn'] < lower_limit, lower_limit, df['Qty in OPUn'])))
sns.boxplot(replace_val)

#################### NORMALIZATION ########################

from sklearn.preprocessing import MinMaxScaler
###data = pd.read_excel('data.xlsx')
scaler = MinMaxScaler()
df['Qty in OPUn'] = scaler.fit_transform(df[['Qty in OPUn']])
print(df)

############### TRANSFORMATION ##########################
df['Value_log2'] = np.log(df['Qty in OPUn'])
print(df)


############## First/ Second/ Third/ Fourth  Moment Business Decision ############


df['Qty in order unit'] = pd.to_numeric(df['Qty in order unit'], errors = 'coerce')

df['Qty in order unit'].mean()
df['Qty in order unit'].median()
df['Qty in order unit'].mode()
df['Qty in order unit'].std()
df['Qty in order unit'].var()
df['Qty in order unit'].max() - df['Qty in order unit'].min()
df['Qty in order unit'].skew()
df['Qty in order unit'].kurt()


################ GRAPHICAL REPRESENTATION ################

import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
plt.hist(df['Qty in order unit'],bins = 20 )
plt.title("Qty in order unit")
plt.tight_layout()
plt.show()


####################### Q-Q PLOT ##############

import seaborn as sns
import scipy.stats as stats


data = np.random.normal(loc=0, scale=1, size=1000)

plt.figure(figsize=(8, 6))
stats.probplot(df['Qty in order unit'], dist="norm", plot=plt)
plt.title("Q-Q Plot", fontsize=16)
plt.grid(True)
plt.show()

################### DENSITY PLOT ##################
plt.figure(figsize=(8, 6))
sns.kdeplot(df['Qty in order unit'], fill=True, color='blue', alpha=0.5)
plt.title("Density Plot", fontsize=16)
plt.xlabel("Data", fontsize=12)
plt.ylabel("Density", fontsize=12)
plt.grid(True)
plt.show()
############## DUPLICATES ##############

df.drop_duplicates (keep = 'first')
print(df)

########### MISSING VALUES ###########

missing_values = df['Qty in order unit'].isnull().any()
print("missing values present in:", missing_values)

################# OUTLIER ##################

import seaborn as sns

sns.boxplot(df['Qty in order unit'])
IQR = df['Qty in order unit'].quantile(0.75) - df['Qty in order unit'].quantile(0.25)
lower_limit = df['Qty in order unit'].quantile(0.25) - (IQR * 1.5)
upper_limit = df['Qty in order unit'].quantile(0.75) + (IQR * 1.5)

#Replace the outliers by the maximum and minimum limit
replace_val = pd.DataFrame(np.where(df['Qty in order unit'] > upper_limit, upper_limit, np.where(df['Qty in order unit'] < lower_limit, lower_limit, df['Qty in order unit'])))
sns.boxplot(replace_val)

#################### NORMALIZATION ########################

from sklearn.preprocessing import MinMaxScaler
###data = pd.read_excel('data.xlsx')
scaler = MinMaxScaler()
df['Qty in order unit'] = scaler.fit_transform(df[['Qty in order unit']])
print(df)

############### TRANSFORMATION ##########################
df['Value_log3'] = np.log(df['Qty in order unit'])
print(df)



############## First/ Second/ Third/ Fourth  Moment Business Decision ############


df['Amount in LC'] = pd.to_numeric(df['Amount in LC'], errors = 'coerce')

df['Amount in LC'].mean()
df['Amount in LC'].median()
df['Amount in LC'].mode()
df['Amount in LC'].std()
df['Amount in LC'].var()
df['Amount in LC'].max() - df['Amount in LC'].min()
df['Amount in LC'].skew()
df['Amount in LC'].kurt()

################ GRAPHICAL REPRESENTATION (HISTOGRAM) ################

import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
plt.hist(df['Amount in LC'],bins = 20 )
plt.title("Amount in LC")
plt.tight_layout()
plt.show()

############## DUPLICATES ##############

df.drop_duplicates (keep = 'first')
print(df)

########### MISSING VALUES ###########

missing_values = df['Amount in LC'].isnull().any()
print("missing values present in:", missing_values)


####################### Q-Q PLOT ##############

import seaborn as sns
import scipy.stats as stats


data = np.random.normal(loc=0, scale=1, size=1000)

plt.figure(figsize=(8, 6))
stats.probplot(df['Amount in LC'], dist="norm", plot=plt)
plt.title("Q-Q Plot", fontsize=16)
plt.grid(True)
plt.show()

################### DENSITY PLOT ##################
plt.figure(figsize=(8, 6))
sns.kdeplot(df['Amount in LC'], fill=True, color='blue', alpha=0.5)
plt.title("Density Plot", fontsize=16)
plt.xlabel("Data", fontsize=12)
plt.ylabel("Density", fontsize=12)
plt.grid(True)
plt.show()

################# OUTLIER ##################

import seaborn as sns

sns.boxplot(df['Amount in LC'])
IQR = df['Amount in LC'].quantile(0.75) - df['Amount in LC'].quantile(0.25)
lower_limit = df['Amount in LC'].quantile(0.25) - (IQR * 1.5)
upper_limit = df['Amount in LC'].quantile(0.75) + (IQR * 1.5)

#Replace the outliers by the maximum and minimum limit
replace_val = pd.DataFrame(np.where(df['Amount in LC'] > upper_limit, upper_limit, np.where(df['Amount in LC'] < lower_limit, lower_limit, df['Amount in LC'])))
sns.boxplot(replace_val)


#################### NORMALIZATION ########################

from sklearn.preprocessing import MinMaxScaler
###data = pd.read_excel('data.xlsx')
scaler = MinMaxScaler()
df['Amount in LC'] = scaler.fit_transform(df[['Amount in LC']])
print(df)

############### TRANSFORMATION ##########################
df['Value_log4'] = np.log(df['Amount in LC'])
print(df)


############## First/ Second/ Third/ Fourth  Moment Business Decision ############


df['Quantity'] = pd.to_numeric(df['Quantity'], errors = 'coerce')

df['Quantity'].mean()
df['Quantity'].median()
df['Quantity'].mode()
df['Quantity'].std()
df['Quantity'].var()
df['Quantity'].max() - df['Quantity'].min()
df['Quantity'].skew()
df['Quantity'].kurt()

################ GRAPHICAL REPRESENTATION ################

import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
plt.hist(df['Quantity'],bins = 20 )
plt.title("Quantity")
plt.tight_layout()
plt.show()

####################### Q-Q PLOT ##############

import seaborn as sns
import scipy.stats as stats


data = np.random.normal(loc=0, scale=1, size=1000)

plt.figure(figsize=(8, 6))
stats.probplot(df['Quantity'], dist="norm", plot=plt)
plt.title("Q-Q Plot", fontsize=16)
plt.grid(True)
plt.show()

################### DENSITY PLOT ##################
plt.figure(figsize=(8, 6))
sns.kdeplot(df['Quantity'], fill=True, color='blue', alpha=0.5)
plt.title("Density Plot", fontsize=16)
plt.xlabel("Data", fontsize=12)
plt.ylabel("Density", fontsize=12)
plt.grid(True)
plt.show()


############## DUPLICATES ##############

df.drop_duplicates (keep = 'first')
print(df)

########### MISSING VALUES ###########

missing_values = df['Quantity'].isnull().any()
print("missing values present in:", missing_values)

################# OUTLIER ##################

import seaborn as sns

sns.boxplot(df['Quantity'])
IQR = df['Quantity'].quantile(0.75) - df['Quantity'].quantile(0.25)
lower_limit = df['Quantity'].quantile(0.25) - (IQR * 1.5)
upper_limit = df['Quantity'].quantile(0.75) + (IQR * 1.5)

#Replace the outliers by the maximum and minimum limit
replace_val = pd.DataFrame(np.where(df['Quantity'] > upper_limit, upper_limit, np.where(df['Quantity'] < lower_limit, lower_limit, df['Quantity'])))
sns.boxplot(replace_val)

#################### NORMALIZATION ########################

from sklearn.preprocessing import MinMaxScaler
###data = pd.read_excel('data.xlsx')
scaler = MinMaxScaler()
df['Quantity'] = scaler.fit_transform(df[['Quantity']])
print(df)

############### TRANSFORMATION ##########################
df['Value_log5'] = np.log(df['Quantity'])
print(df)

