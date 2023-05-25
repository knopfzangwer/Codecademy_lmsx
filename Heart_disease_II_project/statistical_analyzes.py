# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind, f_oneway, chi2_contingency
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# load data
heart = pd.read_csv('heart_disease.csv')

# Task 1
print(heart.head())

# Task 2
sns.boxplot(x="heart_disease", y="thalach", data=heart)
plt.xlabel("Heart Disease")
plt.title("Heart disease vs thalach")
plt.show()
plt.clf()

# Task 3
thalach_hd = heart.thalach[heart.heart_disease == "presence"]
thalach_no_hd = heart.thalach[heart.heart_disease == "absence"]

# Task 4
print("The difference between the mean of thalach for pacients diagnosed with heart"
      " disease compared to the patients without it is {}".format(np.mean(thalach_hd)-np.mean(thalach_no_hd)))

print("The difference between the median of thalach for pacients diagnosed with heart"
      " disease compared to the patients without it is {}".format(np.median(thalach_hd)-np.median(thalach_no_hd)))

# Task 5 (imported at the begin) and 6
tstat, pval = ttest_ind(thalach_hd, thalach_no_hd)
print(pval)
print("The p-value is {}, so if it's below the threshold of 0.05, the null hypotesis is rejected"
      " and the alternative hypotesis should fit better in this case".format(pval))

# Task 7
sns.boxplot(x="heart_disease", y="age", data=heart)
plt.title("Heart disease vs age")
plt.xlabel("Heart Disease")
plt.show()
plt.clf()

sns.boxplot(x="heart_disease", y="trestbps", data=heart)
plt.title("Heart disease vs resting blood pressure (trestbps)")
plt.xlabel("Heart Disease")
plt.show()
plt.clf()

sns.boxplot(x="heart_disease", y="chol", data=heart)
plt.title("Heart disease vs serum cholesterol (chol)")
plt.xlabel("Heart Disease")
plt.show()
plt.clf()

# Task 8
sns.boxplot(x="cp", y="thalach", data=heart)
plt.title("Type of heart pain vs thalach")
plt.xlabel("Type of heart pain")
plt.show()
plt.clf()

# Task 9
thalach_typical = heart.thalach[heart.cp == "typical angina"]
thalach_asymptom = heart.thalach[heart.cp == "asymptomatic"]
thalach_nonangin = heart.thalach[heart.cp == "non-anginal pain"]
thalach_atypical = heart.thalach[heart.cp == "atypical angina"]

# The use of ANOVA here is useful!
fstat, pval = f_oneway(thalach_typical, thalach_asymptom, thalach_nonangin, thalach_atypical)
print("The p-value is {}, so if it's below the threshold of 0.05, the null hypotesis is rejected"
      " and the alternative hypotesis should fit better in this case".format(pval))

# Task 11
# For this task the use of the Tukey's Range Test is good.
tukey_results = pairwise_tukeyhsd(heart.thalach, heart.cp, 0.05)
print(tukey_results)

# Task 12
# Now the use o Chi-Square is good, because we have two categorical variables to analyze.
Xtab = pd.crosstab(heart.cp, heart.heart_disease)
print(Xtab)

chi2, pval, dof, expected = chi2_contingency(Xtab)
print("The p-value is {}, so if it's below the threshold of 0.05, the null hypotesis is rejected"
      " and the alternative hypotesis should fit better in this case".format(pval))