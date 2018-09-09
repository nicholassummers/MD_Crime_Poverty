# In[1]:
#import modules necessary to perform statistical analysis
import pandas as pd

import numpy as np

import statsmodels.api as sm

import statsmodels.formula.api as smf

#independent variable (x): poverty rates
#dependent variable (y): violent crimes

#poverty rates are in percentages (ex. 7.8 is 7.8%)
#these are actual maryland porverty percentages from 2006 to 2013
x = [7.80,8.30,8.10,9.10,9.90,10.10,10.30,10.10]
#crime measured in number of violent crimes per year(y)
#these are the actual number of violent crimes in maryland from 2006 to 2013
y = [38111,36065,35394,33625,31604,28798,28079,27720]
#perform ordinary least squares linear regression and store results
#stores results as string
results = smf.OLS(y,x).fit()
#print the results to the console
print(results.summary())




